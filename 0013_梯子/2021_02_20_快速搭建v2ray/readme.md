登录vps  
mkdir v2ray  
cd ./v2ray  
mkdir v2ray-v4.31.0  
wget https://github.com/v2fly/v2ray-core/releases/download/v4.31.0/v2ray-linux-64.zip  
unzip ./v2ray-linux-64.zip  
rm ./v2ray-linux-64.zip  
mv ./config.json ./config.json.origin  
vim ./config.json
```
{
    "inbounds": [
        {
            "port": 10086, // 服务器监听端口
            "protocol": "vmess",
            "settings": {
                "clients": [
                    {
                        "id": "b831381d-6324-4d53-ad4f-8cda48b30811"
                    }
                ]
            }
        }
    ],
    "outbounds": [
        {
            "protocol": "freedom"
        }
    ]
}
```
修改端口和id，全路径后台启动v2ray

客户端配置更改为
```
{
    "inbounds": [
        {
            "port": 1080, // SOCKS 代理端口，在浏览器中需配置代理并指向这个端口
            "listen": "127.0.0.1",
            "protocol": "socks",
            "settings": {
                "udp": true
            }
        }
    ],
    "outbounds": [
        {
            "protocol": "vmess",
            "settings": {
                "vnext": [
                    {
                        "address": "server", // 服务器地址，请修改为你自己的服务器 ip 或域名
                        "port": 10086, // 服务器端口
                        "users": [
                            {
                                "id": "b831381d-6324-4d53-ad4f-8cda48b30811"
                            }
                        ]
                    }
                ]
            }
        },
        {
            "protocol": "freedom",
            "tag": "direct"
        }
    ],
    "routing": {
        "domainStrategy": "IPOnDemand",
        "rules": [
            {
                "type": "field",
                "ip": [
                    "geoip:private"
                ],
                "outboundTag": "direct"
            }
        ]
    }
}
```
linux：借助服务实现开机自启，安装方式选择以服务的形式安装，参考：https://github.com/v2fly/fhs-install-v2ray  
windows：借助nssm实现监控且开机自启，安装方式选择自解压即可

参考链接：  
https://www.v2fly.org/guide/start.html  
https://www.v2fly.org/awesome/tools.html
