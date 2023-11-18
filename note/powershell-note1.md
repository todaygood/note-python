
# 改变powershell默认窗口大小

Use a function like this in your profile (notepad $profile)

Function Set-WindowSize {
Param([int]$x=$host.ui.rawui.windowsize.width,
      [int]$y=$host.ui.rawui.windowsize.heigth)

    $size=New-Object System.Management.Automation.Host.Size($x,$y)
    $host.ui.rawui.WindowSize=$size   
}
Then call the function:

Set-WindowSize 100 50

# 后台运行 


开启后台任务
比如在后台执行ping 8.8.8.8

Start-Job -ScriptBlock {ping 8.8.8.8}
从返回可以看到job的基本信息

Id     Name            PSJobTypeName   State         HasMoreData     Location             Command                  
--     ----            -------------   -----         -----------     --------             -------                  
3      Job3            BackgroundJob   Running       True            localhost            ping 8.8.8.8 
除了Start-Job还有可以在远程执行任务的命令Invoke-Command。

查看后台任务
Get-Job
结果如下

Id     Name            PSJobTypeName   State         HasMoreData     Location             Command                  
--     ----            -------------   -----         -----------     --------             -------                             
1      Job1            BackgroundJob   Completed     True            localhost            ping 8.8.8.8
3      Job3            BackgroundJob   Running       True            localhost            Sleep -Seconds 15 
停止后台任务
Stop-Job -Id 3
移除后台任务
Remove-Job -Id 3

