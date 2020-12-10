参考了几篇博客在/usr/share/applications/下写了anyconnect.desktop如下
```
[Desktop Entry]
Name=AnyConnect
Exec=path_to_vpnui
Terminal=false
Type=Application
Icon=path_to_vpnui48.png
#StartupWMClass=baidunetdisk
#Comment=百度网盘
#MimeType=x-scheme-handler/baiduyunguanjia;
#Categories=Network;
```
结果双击anyconnect.desktop后仍不能将启动的anyconnect固定到侧边栏

正当无从下手时，随手点开左下角的“显示应用程序”，看到出现了Cisco AnyConnect的图标，如下图  
![image](./0.png)  
右键点击图标，竟然出现了“固定到收藏夹的选项”，如下图  
![image](./1.png)  
好了，幸运的把问题解决了
