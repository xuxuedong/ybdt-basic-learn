以下方式可用于windows和linux下  
被测试在如下系统：
系统：kali2019_x64_en-us  
系统：win10_pro_x64_zh-chs_commando


burp下导出证书：

方式0：

开启burp的代理，设置firefox代理为burp的地址，然后访问http:/burp/cert

它会自动下载一个文件名为cacer.der

方式1：

burp下找到Proxy->Options->import/export ca certificate，如下图所示

![image](https://github.com/xuxuedong/YBDTBlog_Security/blob/master/2019_09_26_burpsuite%E5%A6%82%E4%BD%95%E4%BB%A3%E7%90%86https%E6%B5%81%E9%87%8F/0.png)

点击import/export ca certificate，选择certificate in der format，然后点击next，如下图所示

![image](https://github.com/xuxuedong/YBDTBlog_Security/blob/master/2019_09_26_burpsuite%E5%A6%82%E4%BD%95%E4%BB%A3%E7%90%86https%E6%B5%81%E9%87%8F/1.png)

点击select file，指定文件名为cacert0.der，点击save，如下图所示

![image](https://github.com/xuxuedong/YBDTBlog_Security/blob/master/2019_09_26_burpsuite%E5%A6%82%E4%BD%95%E4%BB%A3%E7%90%86https%E6%B5%81%E9%87%8F/a.png)

firefox下导入证书：

privacy & security->certificates，如下图所示

![image](https://github.com/xuxuedong/YBDTBlog_Security/blob/master/2019_09_26_burpsuite%E5%A6%82%E4%BD%95%E4%BB%A3%E7%90%86https%E6%B5%81%E9%87%8F/2.png)

view certificates->authorities->import，如下图所示

![image](https://github.com/xuxuedong/YBDTBlog_Security/blob/master/2019_09_26_burpsuite%E5%A6%82%E4%BD%95%E4%BB%A3%E7%90%86https%E6%B5%81%E9%87%8F/3.png)

选择刚才导出的证书即可
