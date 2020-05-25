访问本地的https://127.0.0.1:3443（AWVS）， 通过SwitchyOmega的临时走burp，不能生效  
更改network.proxy.allow_hijacking_localhost的值为true，访问本地的https://127.0.0.1:3443（AWVS）， 通过SwitchyOmega的临时走burp，不能生效  
怀疑可能是firefox下的SwitchyOmega不能代理127.0.0.1，更改firefox的代理设置为“手动代理配置”，network.proxy.allow_hijacking_localhost的值为false，访问https://127.0.0.1:3443， 不能走burp，network.proxy.allow_hijacking_localhost的值为true，访问https://127.0.0.1:3443， 不能走burp  

访问本地的http://127.0.0.1/（nginx）， 通过SwitchyOmega的临时走burp，不能生效  
更改network.proxy.allow_hijacking_localhost的值为true，访问本地的http://127.0.0.1/（nginx）， 通过SwitchyOmega的临时走burp，不能生效  
怀疑可能是firefox下的SwitchyOmega不能代理127.0.0.1，更改firefox的代理设置为“手动代理配置”，更改network.proxy.allow_hijacking_localhost的值为false，访问http://127.0.0.1/（nginx）， 不能走burp，更改network.proxy.allow_hijacking_localhost的值为true，访问http://127.0.0.1/（nginx）， 能走burp  

临时解决方案：  
使用本机局域网ip地址172.16.35.128代替127.0.0.1  
network.proxy.allow_hijacking_localhost的值为false，firefox的代理设置为“使用系统代理设置”，通过SwitchyOmega的临时走burp，访问本地的http://127.0.0.1/（nginx）， 能走burp，访问本地的https://172.16.35.128:3443/（AWVS） 能走burp  
