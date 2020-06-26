事情源于我在一次授权渗透测试中发现一处sql注入漏洞，在爆库是发现有个数据库是中文，当在repeater->request中输入中文时，发现乱码

本以为是我当前使用的kali系统不支持中文字体，结果在win10下尝试仍旧乱码

网上查阅了一些资料，所说的办法无非就是user options->display，改字体，改字符集，在kali和win10下尝试，仍旧无效

本想尝试一些burp extension，结果看完简介后感觉作用都不大，想过尝试汉化版，现在看来，应该也无效

下载最新版的burpsuite_community_windows-x64_v2020_5_1.exe，尝试后发现在repeater->request中输入中文时，不乱码，怀疑可能是官方在某个版本中修复了中文乱码的问题，我之前用的是burpsuite pro v2.1.04破解版，于是我下载了burpsuite_community_windows-x64_v2_1_04.exe，测试后发现乱码，由此可见，官方应该是在v2.1.04之后的某个版本修复了中文乱码的问题

为了一劳永逸，不至于以后在burpsuite pro v2.1.04破解版和burpsuite_community_windows-x64_v2020_5_1.exe切换，网上搜索最新版的破解版，搜到如下这篇文章  
https://xcxmiku.com/archives/38a7a949/
里面提供了burpsuite v2020.5.1破解版，经校验，SHA256都正确，本以为还需要激活一次，结果直接执行start.vbs就可用

【关于下载】  
原文中是用的百度云盘分享的文件，我当时下载超级慢，最后实在不想等了，就办了超级会员，为了避免各位同行有同样问题，这里使用天翼云分享给大家，本人测试发现天翼云还是较快的  
https://cloud.189.cn/t/VfiyyeYZnaQf (访问码:7xtq)  
如果觉得下载帮助了你，请给个star
