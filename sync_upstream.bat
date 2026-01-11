@echo off
chcp 65001 >nul
echo ========================================
echo    同步上游仓库更新脚本
echo ========================================
echo.

:: 检查是否已添加 upstream
git remote get-url upstream >nul 2>&1
if errorlevel 1 (
    echo [INFO] 首次运行，添加 upstream 远程仓库...
    git remote add upstream https://github.com/vnpy/vnpy.git
    if errorlevel 1 (
        echo [ERROR] 添加 upstream 失败
        pause
        exit /b 1
    )
    echo [OK] upstream 添加成功
)

echo.
echo [INFO] 获取上游仓库最新代码...
git fetch upstream
if errorlevel 1 (
    echo [ERROR] 获取上游代码失败，请检查网络连接
    pause
    exit /b 1
)

echo.
echo [INFO] 切换到 master 分支...
git checkout master
if errorlevel 1 (
    echo [ERROR] 切换分支失败，请先提交或暂存本地修改
    pause
    exit /b 1
)

:: 检查是否需要更新
for /f %%i in ('git rev-parse HEAD') do set LOCAL_COMMIT=%%i
for /f %%i in ('git rev-parse upstream/master') do set UPSTREAM_COMMIT=%%i

if "%LOCAL_COMMIT%"=="%UPSTREAM_COMMIT%" (
    echo.
    echo [OK] 已是最新版本，无需更新
    pause
    exit /b 0
)

echo.
echo [INFO] 发现新版本，开始合并...
git merge upstream/master --no-edit
if errorlevel 1 (
    echo.
    echo ========================================
    echo [WARNING] 合并时发生冲突！
    echo.
    echo 请手动解决冲突后执行：
    echo   git add .
    echo   git commit -m "resolve merge conflicts"
    echo   git push origin master
    echo ========================================
    pause
    exit /b 1
)

echo.
echo [INFO] 推送到你的 fork...
git push origin master
if errorlevel 1 (
    echo [ERROR] 推送失败
    pause
    exit /b 1
)

echo.
echo ========================================
echo [OK] 同步完成！
echo ========================================
pause
