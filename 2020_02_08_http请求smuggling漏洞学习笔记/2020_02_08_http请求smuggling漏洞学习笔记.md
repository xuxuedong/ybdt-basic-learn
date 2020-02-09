“http请求smuggling漏洞”原理学习及实验挑战：  
https://portswigger.net/web-security/request-smuggling  

“Chunked transfer encoding”原理学习：  
https://en.wikipedia.org/wiki/Chunked_transfer_encoding  

要理解这个漏洞，有些前置知识我们需要掌握：  
0：服务器端是如何判断一个http请求（包括head和body）的结束？  
首先我们都知道，http header和body之间需要有一个空行，其次body中到底有多少个字节，是取决于Content-Length或Transfer-Encoding中指定的数值，其中Transfer-Encoding并不是直接指定数值（具体格式参照上述“Chunked transfer encoding”原理学习），另外，如果两者同时存在，那么Content-Length头应该被忽略
