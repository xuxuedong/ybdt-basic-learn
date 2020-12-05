vim /etc/network/interfaces修改完静态ip后  
sudo systemctl restart networking无效  
原因未知

解决方案：  
vim /etc/network/interfaces修改完静态ip后  
sudo ip addr flush dev "网卡名"  
sudo ifup "网卡名"
