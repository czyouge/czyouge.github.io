(() => {
  const root = document.documentElement;
  const toggle = document.querySelector('.theme-toggle');
  const preference = matchMedia('(prefers-color-scheme: dark)');
  const saved = (() => {try {return localStorage.getItem('czyouge-theme');} catch {return null;}})();
  if (saved === 'dark' || saved === 'light') root.dataset.theme = saved;
  function syncTheme() {
    const dark = root.dataset.theme ? root.dataset.theme === 'dark' : preference.matches;
    toggle?.setAttribute('aria-pressed', String(dark));
    toggle?.setAttribute('aria-label', dark ? '切换浅色模式' : '切换深色模式');
  }
  syncTheme();
  preference.addEventListener('change', syncTheme);
  toggle?.addEventListener('click', () => {
    root.dataset.theme = toggle.getAttribute('aria-pressed') === 'true' ? 'light' : 'dark';
    try {localStorage.setItem('czyouge-theme', root.dataset.theme);} catch {}
    syncTheme();
  });
  // A collapsed directory leaves more reading room on a phone.
  const toc = document.querySelector('.toc details');
  if (toc && matchMedia('(max-width: 760px)').matches) toc.open = false;
  const form = document.querySelector('.search-form');
  if (!form) return;
  const input = document.getElementById('search-input');
  const status = document.getElementById('search-status');
  const results = document.getElementById('search-results');
  let indexPromise;
  let sequence = 0;
  const normalize = value => value.normalize('NFKC').toLocaleLowerCase();
  function element(tag, text, className) {
    const node = document.createElement(tag);
    if (text) node.textContent = text;
    if (className) node.className = className;
    return node;
  }
  async function search(query) {
    const id = ++sequence;
    results.replaceChildren();
    query = query.trim();
    if (!query) {status.textContent = '搜索覆盖全部已发布文章的标题与正文。'; return;}
    status.textContent = '正在搜索…';
    try {
      indexPromise ||= fetch('/index.json').then(response => {
        if (!response.ok) throw Error('index unavailable');
        return response.json();
      }).catch(error => {indexPromise = null; throw error;});
      const entries = await indexPromise;
      if (id !== sequence) return;
      const words = normalize(query).split(/\s+/).filter(Boolean);
      const matches = entries.map(entry => {
        const title = normalize(entry.title);
        const tags = normalize(entry.tags.join(' '));
        const body = normalize(entry.text);
        if (!words.every(word => title.includes(word) || tags.includes(word) || body.includes(word))) return null;
        const score = words.reduce((sum, word) => sum + (title.includes(word) ? 10 : 0) + (tags.includes(word) ? 5 : 0), 0);
        return {entry, score};
      }).filter(Boolean).sort((a,b) => b.score - a.score || b.entry.date.localeCompare(a.entry.date));
      status.textContent = `找到 ${matches.length} 篇相关文章`;
      for (const {entry} of matches) {
        const article = element('article', '', 'search-result');
        const heading = element('h2');
        const link = element('a', entry.title);
        link.href = entry.url;
        heading.append(link);
        const first = normalize(entry.text).indexOf(words[0]);
        const start = Math.max(0, first - 35);
        const excerpt = (start ? '…' : '') + entry.text.slice(start, start + 140).replace(/\s+/g, ' ') + '…';
        article.append(heading, element('p', excerpt), element('time', entry.date));
        results.append(article);
      }
      if (!matches.length) results.append(element('p', '试试更短的关键词，或到归档中按年份浏览。'));
    } catch {
      if (id === sequence) status.textContent = '暂时无法读取搜索索引，请稍后重试，或通过归档浏览文章。';
    }
  }
  form.addEventListener('submit', event => {
    event.preventDefault();
    const url = new URL(location.href);
    url.searchParams.set('q', input.value.trim());
    history.replaceState(null, '', url);
    search(input.value);
  });
  const initial = new URLSearchParams(location.search).get('q') || new URLSearchParams(location.search).get('tag');
  if (initial) {input.value = initial; search(initial);}
})();
