chrome不能启动：  
vim /opt/google/chrome/google-chrome  
最后一行改为：  
exec -a "$0" "$HERE/chrome" "$@" --no-sandbox  
参考链接：  
https://conimi.com/archives/51/

安装SwitchyOmega：  
命令行执行：  
google-chrome --proxy-server="http://127.0.0.1:8080"  
到chrome商店中搜索SwitchyOmega并安装  
参考链接：  
https://blog.csdn.net/qq_30101131/article/details/84641200
