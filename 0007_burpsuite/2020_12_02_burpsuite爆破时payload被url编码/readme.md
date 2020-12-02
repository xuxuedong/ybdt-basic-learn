墨者学院中的一道题，地址如下：  
https://www.mozhe.cn/bug/detail/WTNpdGxUS3l4dG9uMFF6ZEs3OEJCdz09bW96aGUmozhe  
在使用burp的intruder时，返回数据包中发现提示“ip违法”，进一步查看，请求的ip地址“128.0.0.2”被编码为“128%2e0%2e0%2e2”  
解决方式：  
Intruder->Payloads->Payload Encoding中的“.”去掉
