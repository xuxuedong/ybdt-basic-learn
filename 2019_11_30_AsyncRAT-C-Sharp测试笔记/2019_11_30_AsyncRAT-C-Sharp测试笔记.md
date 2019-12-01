最后更新时间：2019/12/01 10：04

测试环境：

软件版本：v0.5.4H  
服务端：win10_pro_x64_zh-chs_commando  
被控端：win10_pro_x64_zh-chs  
被控端：win7_ult_x64_zh-chs  
被控端：xp_pro_x86_zh-chs

软件安装测试结果：  
官网上提到了“AsyncRAT requires the .Net Framework v4 (client) and v4.6+ (server) to run.”  
经测试，在win10下默认即可使用，但在win7和xp下，默认是没有.Net Framework v4的，所以执行后，如果客户机没装.Net Framework v4则会报错，如下图  
![image](https://github.com/xuxuedong/YBDTBlog_Security/blob/master/2019_11_30_AsyncRAT-C-Sharp%E6%B5%8B%E8%AF%95%E7%AC%94%E8%AE%B0/0.png)

免杀测试结果：  
使用https://github.com/NYAN-x-CAT/AsyncRAT-C-Sharp/releases/download/v0.5.4H/AsyncRAT.v0.5.4H.zip的服务端生成的客户端  
可绕过360的静态查杀  
不能绕过defender的静态查杀

使用过程测试结果：  
0：发现一个远程桌面相关的问题，当client.exe以非uac绕过的权限执行时，且目标打开任务管理器（或资源监视器）时，即使开启鼠标操作，也无法用鼠标
操作远程桌面（跟QuasarRAT中的问题一样）

总体来说，还是一个不错的rat，还有很多功能有待发现
