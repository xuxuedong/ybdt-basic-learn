漏洞产生原因：  
开发人员使用git进行版本控制，在部署生产环境时直接pull整个项目，导致.git文件夹也被pull，由此导致的.git文件夹泄漏漏洞  

漏洞利用方式：  
使用师傅lijiejie的项目GitHack，地址https://github.com/lijiejie/GitHack  
下载项目到本地后  
cd ./GitHack-master  #项目使用python2编写，所以执行时要使用python2  
python ./GitHack.py http://124.126.19.106:31232/.git/  #此时使用的是攻防世界中->web高级->lottery这道题的环境  
执行完后，文件会被下载到如下目录下  
![image]("./2020-05-26 16-43-33 的屏幕截图.png")  
