app渗透测试学习来源：
https://mp.weixin.qq.com/s/xtzfbmDQXHx_A9nvTVpgzQ

个人总结“移动端渗透测试相比web段渗透测试”的不同之处：  

0：如果对iphone上的app进行渗透测试，则需要进一步让iphone信任burp的证书  
[参考我的如下文章](https://github.com/xuxuedong/YBDTBlog_Security/blob/master/2019_09_26_burpsuite%E5%A6%82%E4%BD%95%E4%BB%A3%E7%90%86https%E6%B5%81%E9%87%8F/2019_12_13_burp%E4%BB%A3%E7%90%86ios%E4%B8%8Bsafari%E7%9A%84https%E6%B5%81%E9%87%8F.md)  

1：如果app发往服务端的数据包是经过加密的，则需要反编译app，查看加密方式及密钥（通常是md5、aes加密）  
