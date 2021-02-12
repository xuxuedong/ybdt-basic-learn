针对操作系统：ubuntu 18.04

安装数据库  
apt install mariadb-server#截止到2020.10.07,安装好之后，会安装mariadb-client-10.1和mariadb-server-10.1  
systemctl status mariadb#安装好之后会自动启动，执行此命令可检查是否启动  
systemctl enable mariadb#设为开机自启  
mysql_secure_installation#执行此命令来加固mariadb  
参考链接：  
https://www.myfreax.com/how-to-install-mariadb-on-ubuntu-18-04/

安装中间件php7.2及相关依赖  
apt install php7.2-cli php7.2-fpm php7.2-mysql php7.2-json php7.2-opcache php7.2-mbstring php7.2-xml php7.2-gd php7.2-curl

安装配置WEB服务器  
apt install nginx  
```
/etc/nginx/nginx.conf会include /etc/nginx/conf.d/*.conf;和include /etc/nginx/sites-enabled/*; 
```
我的配置一开始放到了/etc/nginx/conf.d/ybdt.conf中，后来放到了/etc/nginx/sites-enabled/default中  
配置文件出错，fastcgi_pass unix:/var/run/php/php7.2-fpm.sock;写成了fastcgi_pass unix:/var/run/php/php7.0-fpm.sock;导致访问网站502，排查了很长时间

安装配置SSL证书  
apt install python3 && apt install python3-pip && pip3 install certbot  
certbot --help#检查certbot是否成功安装  
certbot certonly --standalone -d tlanyan.me -d www.tlanyan.me#执行此命令获取证书  
systemctl stop nginx && certbot renew && systemctl restart nginx#每隔3个月需要手动续期  
参考链接：  
https://tlanyan.me/use-lets-encrypt-certificate/

安装配置CMS  
cd /var/www/html/  
mkdir ./ybdt.best/  
cd /ybdt.best/  
wget https://wordpress.org/latest.tar.gz  
tar -xvf ./latest.tar.gz  
rm ./latest.tar.gz  
cd ../  
chown -R www-data: ./ybdt.best/

配置数据库  
create database xxx;  
安装wordpress时用root用户连接数据库失败，需要创建新用户  
create user 'xxx'@'localhost' identified by 'xxx';  
grant all on xxx.* to 'xxx'@'localhost';  
参考链接：  
https://www.cnblogs.com/zhongyehai/p/10695659.html

v2ray无效了，经过研究发现，由于域名www.ybdt.best强制重定向为ybdt.best，导致本地v2ray客户端不能找到目标，所以提示301  

参考链接：  
https://www.myfreax.com/how-to-install-wordpress-with-nginx-on-ubuntu-18-04/  
https://www.digitalocean.com/community/tutorials/how-to-install-wordpress-with-lemp-on-ubuntu-18-04  
https://www.rsyncd.net/348.html  
https://blog.csdn.net/u013474436/article/details/52972699
