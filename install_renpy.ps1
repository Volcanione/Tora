$url = "https://www.renpy.org/dl/8.3.4/renpy-8.3.4-sdk.zip"
$output = "renpy-sdk.zip"
$extractPath = "d:/学习/python/renpy_sdk"

Write-Host "正在从 $url 下载 Ren'Py SDK..."
Invoke-WebRequest -Uri $url -OutFile $output

Write-Host "正在解压到 $extractPath..."
Expand-Archive -Path $output -DestinationPath $extractPath -Force

Write-Host "安装完成！"
Write-Host "您可以运行 $extractPath/renpy-8.3.4-sdk/renpy.exe 来启动 Ren'Py Launcher。"
Remove-Item $output
