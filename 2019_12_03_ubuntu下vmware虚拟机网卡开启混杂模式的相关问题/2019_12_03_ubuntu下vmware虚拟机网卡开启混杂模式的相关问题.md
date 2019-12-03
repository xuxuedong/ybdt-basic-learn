最初是在虚拟机中使用goby时提示的“网卡混杂的问题”，问题如下  
![image](https://github.com/xuxuedong/YBDTBlog_Security/blob/master/2019_12_03_ubuntu%E4%B8%8Bvmware%E8%99%9A%E6%8B%9F%E6%9C%BA%E7%BD%91%E5%8D%A1%E5%BC%80%E5%90%AF%E6%B7%B7%E6%9D%82%E6%A8%A1%E5%BC%8F%E7%9A%84%E7%9B%B8%E5%85%B3%E9%97%AE%E9%A2%98/2019-12-03%2014-31-43%20%E7%9A%84%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE.png)
然后不记得如何操作的，最终修改/etc/vmnet*的权限为rw-rw-rw-

后来使用wireshark时再一次提示“网卡混杂的问题”  
此时发现，修改/etc/vmnet*的权限后，重启时，权限会恢复为rw-rw-rw-

通过查阅资料可知  
此时的权限是可以让虚拟机的网卡开启混杂模式的，至于为什么还提示，可能只是提示，并没有禁止，如果不确定的话可以执行  
ifconfig -a来查看网卡是否处于混杂模式（查看是否有PROMISC），还可手动开启关闭  
ifconfig eth0 promisc  
ifconfig eth0 -promisc
