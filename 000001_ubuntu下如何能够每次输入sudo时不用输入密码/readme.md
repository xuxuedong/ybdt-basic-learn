ls -alh /etc/sudoers  

sudo chmod u+w /etc/sudoers  

sudo vim /etc/sudoers  #将表示sudo组那一行改为如下  
%sudo   ALL=(ALL:ALL) NOPASSWD:ALL  

sudo chmod u-w /etc/sudoers  

over!!!
