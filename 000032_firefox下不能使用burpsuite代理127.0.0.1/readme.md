访问本地的https://127.0.0.1:3443（AWVS）， 通过SwitchyOmega走burp，不能生效  
更改network.proxy.allow_hijacking_localhost的值为true，访问本地的https://127.0.0.1:3443 （AWVS），通过SwitchyOmega走burp，不能生效  
怀疑可能是firefox下的SwitchyOmega不能代理127.0.0.1，更改firefox的代理设置为手动代理配置，访问https://127.0.0.1:3443， 仍不能走burp  

访问本地的http://127.0.0.1/（nginx）， 通过SwitchyOmega走burp，不能生效  
更改network.proxy.allow_hijacking_localhost的值为true，访问本地的http://127.0.0.1/（nginx）， 通过SwitchyOmega走burp，不能生效  
更改network.proxy.allow_hijacking_localhost的值为false，怀疑可能是firefox下的SwitchyOmega不能代理127.0.0.1，更改firefox的代理设置为手动代理配置，访问https://127.0.0.1:3443， 能走burp  
