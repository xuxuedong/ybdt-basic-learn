题目来源：绿盟网络攻防平台

考点1/1：  
如何获取windows xp下LM-Hash：  
实验环境：2003_ent_x86_zh-chs  
下载mimikatz，执行Win32下mimikatz.exe，输入“privilege::debug”会报错，但输入“sekurlsa::logonpasswords”能成功获取到LM-Hash

个人补充：  
如何获取win10下的NTLM-Hash：  
实验环境：win10_pro_x64_zh-chs  
下载mimikatz，以管理员权限执行x64下mimikatz.exe，先输入“privilege::debug”，再输入“sekurlsa::logonpasswords”，成功获取到NTLM-Hash

知识点补充：  
早期SMB协议在网络上传输明文口令，后来出现"LAN Manager Challenge/Response" 验证机制，简称LM，它是如此简单以至很容易被破解。微软提出了WindowsNT挑战/响应验证机制，称之为NTLM。现在已经有了更新的NTLMv2以及Kerberos验证体系。  
对于早期的系统如XP、server 2003来说系统默认使用LM Hash进行加密，也可人为设置成NTLM Hash，之后的server 2008、win7等操作系统禁用了LM Hash，默认使用NTLM Hash，在后续 windows 版本中LM Hash默认存储为空即AAD3B435B51404EEAAD3B435B51404EE  
参考链接：  
https://blog.csdn.net/fanwenbo/article/details/2645283  
https://www.freebuf.com/articles/system/224171.html
