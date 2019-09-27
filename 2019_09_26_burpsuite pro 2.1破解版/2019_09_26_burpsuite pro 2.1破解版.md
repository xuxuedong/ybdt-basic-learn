kali2019_x64_en-us下使用jdk11打开burpsuite时，提示可能会有问题，故改用jdk8打开

![image](https://github.com/xuxuedong/YBDTBlog_Security/blob/master/2019_09_26_burpsuite%20pro%202.1%E5%A6%82%E4%BD%95%E7%A0%B4%E8%A7%A3/0.png)

经查看，kali2019_x64_en-us下存在jdk8，且路径如下/usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java

破解版的burpsuite pro下载链接如下https://pan.baidu.com/s/1SE4dyITO2uT7kLOyzW17sA
提取码fg63（链接永久有效），下载后进入其目录下

执行如下命令/usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java -jar ./burpsuite_pro_v2.1_BurpHelper.jar，如下图所示

![image](https://github.com/xuxuedong/YBDTBlog_Security/blob/master/2019_09_26_burpsuite%20pro%202.1%E5%A6%82%E4%BD%95%E7%A0%B4%E8%A7%A3/1.png)

点击Run，如下图所示

![image](https://github.com/xuxuedong/YBDTBlog_Security/blob/master/2019_09_26_burpsuite%20pro%202.1%E5%A6%82%E4%BD%95%E7%A0%B4%E8%A7%A3/2.png)

点击I Accept，接下来就和启动burpsuite community基本一致了

参考链接：
http://ximcx.cn/post-110.html

