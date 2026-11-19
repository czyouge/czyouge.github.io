@echo off
chcp 65001 >nul
echo 请按提示打开 GitHub 页面并完成登录。不要把密码或令牌发给他人。
git credential-manager github login --username czyouge --device --force --no-ui
pause
