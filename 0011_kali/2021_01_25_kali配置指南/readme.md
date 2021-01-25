0、通过设置，执行sudo时不用输入密码
su - root
chmod u+w /etc/sudoers
将对应行改为：%sudo ALL=(ALL:ALL) NOPASSWD:ALL
chmod u-w /etc/sudoers

1、更改源为阿里源（https://developer.aliyun.com/mirror/）
sudo mv /etc/apt/sources.list /etc/apt/sources.list.bak
sudo vim /etc/apt/sources.list

2、通过设置，让kali系统不自动锁屏、休眠

3、安装chrome（https://www.google.com/intl/zh-CN/chrome/）
dpkg -i ./google-chrome-stable_current_amd64.deb

4、宿主机到虚拟机的复制粘贴有时会失效，故创建共享文件夹
通过vmware设置共享目录
sudo apt install open-vm-tools-desktop fuse
vmware-hgfsclient查看一下
sudo /usr/bin/vmhgfs-fuse .host:/ /mnt/ -o subtype=vmhgfs-fuse,allow_other
将“sudo /usr/bin/vmhgfs-fuse .host:/ /mnt/ -o subtype=vmhgfs-fuse,allow_other”添加到~/.zshrc（注意最新版是ZSH）

5、终端中的字体非常小，太累眼睛
Settings（设置）->Appearance（外观）->Fonts（字体）->DPI改为150

6、


开机自动开启终端更新系统

