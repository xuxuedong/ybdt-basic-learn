最后更新时间：2019/12/01 10：04

测试环境：  
软件版本：v0.5.4H  
服务端：win10_pro_x64_zh-chs_commando  
被控端：win10_pro_x64_zh-chs  
被控端：win7_ult_x64_zh-chs  
被控端：xp_pro_x86_zh-chs

软件安装测试结果：    
0：官网上提到了“AsyncRAT requires the .Net Framework v4 (client) and v4.6+ (server) to run.”经测试，在win10下默认即可使用，但在win7和xp
下，默认是没有.Net Framework v4的，我的虚拟机中xp安装了.Net Framework v4，所以能够正常执行，但win7没有装.Net Framework v4，则报错如下图  
![image](https://github.com/xuxuedong/YBDTBlog_Security/blob/master/2019_11_30_AsyncRAT-C-Sharp%E6%B5%8B%E8%AF%95%E7%AC%94%E8%AE%B0/0.png)

免杀测试结果：  
使用 https://github.com/NYAN-x-CAT/AsyncRAT-C-Sharp/releases/download/v0.5.4H/AsyncRAT.v0.5.4H.zip 的服务端生成的客户端  
0：不添加任何额外选项生成的客户端，能过360的静态查杀  
1：不添加任何额外选项生成的客户端，不能过defender的查杀  
2：勾选build中的simple obfuscator生成的客户端，也不能过defender的查杀  
3：勾选misc中的anti analysis和process critica，以及勾选build中的simple obfuscator，还是不能绕过defender的查杀

使用过程测试结果：  
0：发现一个远程桌面相关的问题，当client.exe以非uac绕过的权限执行时，且目标打开任务管理器（或资源监视器）时，即使开启鼠标操作，也无法用鼠标
操作远程桌面（跟QuasarRAT中的问题一样）  
1：对于被控端是xp系统时，不能查看远程桌面等操作  
2：创建客户端时的第一步Connection部分，除了可以将服务端写死在客户端内，还可以使用第三方的pastebin，这种方式对于服务端有变更，但对客户端
无法操作时，尤其有用（注：服务端可以监听在多个端口，所以客户端写死或者pastebin中也可使用多个端口）  
3：持久化的方式，有一种方式（也可能只有这一种方式）是文件落地到%appdata%，然后注册表键“计算机\HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run”中添加值项，值为“文件落地的路径”，但是重启后会被defender查杀
