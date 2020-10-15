1、尝试通过服务关闭：  
找到服务Windows Defender Antivirus Service后，“停止”按钮是灰色的，不能点击

2、尝试通过组策略关闭：  
gpedit.msc-》计算机配置-》管理模板-》Windows 组件-》Windows Defender 防病毒程序——右侧中的“关闭 Windows Defender 防病毒程序”配置为“已启用”，启用后会生效，但重启后又会恢复到原来的配置

3、尝试通过注册表关闭：  
local machine->software->policies->microsoft->windows defender——新建32位dword值，名为DisableAntiSpyware，值为1(10进制），创建完成后会生效，但重启几次后又会恢复到原来的配置

使用工具Dism++可成功关闭，且重启多次后也不会恢复配置  
使用方法：启动程序-》系统优化-》安全相关设置-》将“禁用Windows Defender”开启
