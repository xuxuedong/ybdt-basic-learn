起因：  
源于我通过ipad连接win10的时候，win10会自动锁屏，登陆win10后，ipad又会自动退出，反复登陆感觉太麻烦，故有此文  

使用stascorp的rdpwrap，官网的仓库（https://github.com/stascorp/rdpwrap/）现在已经被关闭了，幸亏我之前存了一份  

解压后执行RDPConf.exe，在弹出的界面中取消勾选“Single session per user”，其他不用动，其中的Diagnostics部分会告诉你诊断结果  

如果提示你未受支持，是因为你的远程桌面服务的版本大于它默认配置文件中所包含的最高版本，则需要用rdpwrap.ini（https://github.com/sebaxakerhtc/rdpwrap）替换C:\Program Files\RDP Wrapper\下的rdpwrap.ini  

再次执行RDPConf.exe，没问题后执行install.bat，执行完之后重启计算机，然后执行RDPCheck.exe检查一下是否开启成功  
