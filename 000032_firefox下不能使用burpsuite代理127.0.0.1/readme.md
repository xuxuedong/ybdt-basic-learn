尝试过访问about:config，然后更改network.proxy.allow_hijacking_localhost的值为true，仍不能代理https://127.0.0.1:3443

后怀疑可能是firefox下使用的SwitchyOmega不能代理127.0.0.1，更改firefox的代理设置为手动代理配置，仍不能代理https://127.0.0.1:3443
