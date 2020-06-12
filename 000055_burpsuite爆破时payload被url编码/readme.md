墨者中微信投票的一道题，地址如下：  
https://www.mozhe.cn/bug/detail/WTNpdGxUS3l4dG9uMFF6ZEs3OEJCdz09bW96aGUmozhe

2个考点：  
1：修改User-Agent绕过“微信端检测”，可参考我的如下链接：  
https://github.com/xuxuedong/yibudengtian-output-db/tree/master/000002_%E5%A6%82%E4%BD%95%E7%BB%95%E8%BF%87%E2%80%9C%E8%AF%B7%E5%9C%A8%E5%BE%AE%E4%BF%A1%E5%AE%A2%E6%88%B7%E7%AB%AF%E6%89%93%E5%BC%80%E9%93%BE%E6%8E%A5%E2%80%9D%E7%9A%84%E9%99%90%E5%88%B6  
2：修改X-Forwarded-For绕过“每日投票次数限制”

编写脚本生成ip地址，脚本如下：
```
with open("ip-lists.txt", "a") as f:
    for i in range(1, 256):
        ip = "128.0.0." + str(i);
        f.write(ip + "\n");
    for i in range(1, 256):
        ip = "129.0.0." + str(i);
        f.write(ip + "\n");
```

可是在使用burp的intruder时，返回数据包中发现提示“ip违法”，进一步查看，请求的ip地址“128.0.0.1”被编码为“128%2e0%2e0%2e2”  
解决方式：  
Intruder->Payloads->Payload Encoding中的“.”去掉

参考链接：  
https://nocbtm.github.io/2018/07/27/BurpSuit%20%E6%9A%B4%E5%8A%9B%E7%A0%B4%E8%A7%A3%E5%8F%A3%E4%BB%A4/
