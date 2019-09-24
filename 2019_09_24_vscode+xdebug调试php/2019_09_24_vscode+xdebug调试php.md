由于我本机是ubuntu，故实验环境如下：

VMware Workstation 15 Pro for linux（激活码网上可以找到）->https://www.vmware.com/products/workstation-pro.html

08_r2_dat_zh-chs->https://msdn.itellyou.cn/

vscode1.38.1(system setup)->https://code.visualstudio.com/Download

phpstudy2018->https://www.xp.cn/wenda/406.html

thinkphp5.0.22完整版->http://www.thinkphp.cn/donate/download/id/1260.html

xdebug(php_xdebug-2.5.5-5.6-vc11-nts.dll)->https://xdebug.org/files/php_xdebug-2.5.5-5.6-vc11-nts.dll，
（注意，xdebug版本的选择是根据你的php版本，如下为我的php版本信息，5.6.27 + x86 + nts vc11）

![image](https://github.com/xuxuedong/YBDTBlog_Security/blob/master/2019_09_24_vscode%2Bxdebug%E8%B0%83%E8%AF%95php/0.png)



安装vscode，一路下一步即可

安装phpstudy，一路下一步即可，浏览器下访问http://127.0.0.1/，如下所示即安装成功

![image](https://github.com/xuxuedong/YBDTBlog_Security/blob/master/2019_09_24_vscode%2Bxdebug%E8%B0%83%E8%AF%95php/1.png)

将thinkphp5.0.22完整版解压至phpstudy的web目录下，我这里是解压到C:\phpStudy\PHPTutorial\WWW\tp5022下，浏览器下访问http://127.0.0.1/tp5022/public/，如下所示即安装成功

![image](https://github.com/xuxuedong/YBDTBlog_Security/blob/master/2019_09_24_vscode%2Bxdebug%E8%B0%83%E8%AF%95php/2.png)

将下载下来的php_xdebug-2.5.5-5.6-vc11-nts.dll放到php的扩展目录下，即php对应的ext文件夹下，我这里是C:\phpStudy\PHPTutorial\php\php-5.6.27-nts\ext下

配置php.ini的xdebug模块，在php.ini文件末尾的[XDebug]部分中，配置xdebug模块，我这里的配置如下

[XDebug]
zend_extension = php_xdebug-2.5.5-5.6-vc11-nts.dll ; 如果没将php_xdebug-2.5.5-5.6-vc11-nts.dll放到上述目录下，需要指定全路径
xdebug.remote_enable = 1 ; 开启远程调试功能
xdebug.remote_autostart = 1 ; 这个配置是比较重要的一个配置
xdebug.remote_handler = "dbgp" ; 暂时不清楚
xdebug.remote_port = "9001" ; 默认端口号是9000，如果不配置端口号，一旦和其他端口号冲突，容易造成调试器假死状态
xdebug.remote_host = "127.0.0.1" ; 远程调试的ip地址，即你自己的本机ip

重启环境，重新打印phpinfo()，如果phpinfo()中带有xdebug，则安装成功，如下所示

![image](https://github.com/xuxuedong/YBDTBlog_Security/blob/master/2019_09_24_vscode%2Bxdebug%E8%B0%83%E8%AF%95php/3.png)

vscode安装扩展“PHP Debug”

vscode打开thinkphp项目文件夹（）

点击vscode的debug图标，再点击设置图标（我这里由于已经生成过launch.json，所以设置图标会略微不同），会提示选择哪种语言，选择php，它会自动生成launch.json，修改其中的端口号为之前配置的端口号，如下图
![image](https://github.com/xuxuedong/YBDTBlog_Security/blob/master/2019_09_24_vscode%2Bxdebug%E8%B0%83%E8%AF%95php/4.png)
![image](https://github.com/xuxuedong/YBDTBlog_Security/blob/master/2019_09_24_vscode%2Bxdebug%E8%B0%83%E8%AF%95php/5.png)

最好进行调试
