事情源于我在一次授权渗透测试中发现一处sql注入漏洞，在爆库是发现有个数据库是中文，当在repeater->request中输入中文时，发现乱码

本以为是我当前使用的kali系统不支持中文字体，结果在win10下尝试仍旧乱码

网上查阅了一些资料，所说的办法无非就是user options->display，改字体，改字符集，在kali和win10下尝试，仍旧无效

下载最新版的burpsuite_community_windows-x64_v2020_5_1.exe，尝试后发现在repeater->request中输入中文时，不乱码，怀疑可能是官方在某个版本中修复了中文乱码的问题，我之前用的是burpsuite pro v2.1.04破解版 
