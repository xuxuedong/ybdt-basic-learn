最初是在虚拟机中使用goby时提示的“网卡混杂的问题”  
然后不记得如何操作的，最终修改/etc/vmnet*的权限为rw-rw-rw-

后来使用wireshark时再一次提示“网卡混杂的问题”  
此时发现，修改/etc/vmnet*的权限后，重启时，权限会恢复为rw-rw-rw-

通过查阅资料可知  
此时的权限是可以让虚拟机的网卡开启混杂模式的，至于为什么还提示，可能只是提示，并没有禁止，如果不确定的话可以执行  
ifconfig -a来查看网卡是否处于混杂模式（查看是否有PROMISC），还可手动开启关闭  
ifconfig eth0 promisc  
ifconfig eth0 -promisc
