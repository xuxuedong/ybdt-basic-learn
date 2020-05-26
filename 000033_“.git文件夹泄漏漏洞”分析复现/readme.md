漏洞产生原因：  
开发人员使用git进行版本控制，在部署生产环境时直接pull整个项目，导致.git文件夹也被pull，由此导致的.git文件夹泄漏漏洞  

漏洞利用方式：  
使用师傅lijiejie的项目GitHack，地址https://github.com/lijiejie/GitHack  
下载项目到本地后  
cd ./GitHack-master  #项目使用python2编写，所以执行时要使用python2  
python ./GitHack.py http://124.126.19.106:31232/.git/  #此时使用的是攻防世界中->web高级->lottery这道题的环境  
执行完后，文件会被下载到如下目录下  
![image](https://github.com/xuxuedong/yibudengtian-input-db/blob/master/000033_%E2%80%9C.git%E6%96%87%E4%BB%B6%E5%A4%B9%E6%B3%84%E6%BC%8F%E6%BC%8F%E6%B4%9E%E2%80%9D%E5%88%86%E6%9E%90%E5%A4%8D%E7%8E%B0/2020-05-26%2016-43-33%20%E7%9A%84%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE.png)  
下载到的文件如下  
![image](https://github.com/xuxuedong/yibudengtian-input-db/blob/master/000033_%E2%80%9C.git%E6%96%87%E4%BB%B6%E5%A4%B9%E6%B3%84%E6%BC%8F%E6%BC%8F%E6%B4%9E%E2%80%9D%E5%88%86%E6%9E%90%E5%A4%8D%E7%8E%B0/2020-05-26%2017-01-57%20%E7%9A%84%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE.png)  

尝试搭建漏洞环境  
从github中下载项目，将.git文件夹拷贝/root/Desktop/下，执行脚本，脚本报错，根据提示应该放到一个网站目录下  
从github中下载项目，将.git文件夹拷贝到/var/www/html/下，在kali下启动apache2，执行脚本，提示“not found”，原因未知  
