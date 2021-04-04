批处理中的注释是rem  
vbs中的注释是'或rem

for语句在命令行中的基本用法（在批处理中将%i变为%%i）：  
for %i in (set) do command

更高级的用法，强制关闭vscode程序：  
tasklist.exe | findstr "Code.exe">tmp.txt  
type .\tmp.txt  
for /f "tokens=2 delims= " %i in (tmp.txt) do taskkill /pid %i /f /t

更更高级的用法，结合if实现在一行强制关闭vscode程序：  
for /f "tokens=1 delims= " %i in ('tasklist.exe') do @if %i == Code.exe taskkill.exe /im %i /f /t

有如下的问题：  
tasklist.exe | findstr "Code.exe">tmp.txt  
type .\tmp.txt  
for /f "tokens=2 delims= " %i in (tmp.txt) do taskkill /pid %i /f /t  
rem 一开始读取tmp.txt死活读取不到，后来正常了，不知道为什么

for /f %i in ('tasklist.exe') do @echo %i  
rem 默认只输出第一列，觉得应该全部输出啊，不知道为什么  

for /f "tokens=1,2,3,4,5,6 delims= " %i in ('tasklist.exe') do @echo %i %j %k %m %n %o  
rem 输出中会多出%o，经比对发现是tasklist.exe中数字那列没输出，不知道为什么

参考链接：  
https://ss64.com/nt/for_f.html  
https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-xp/bb490920(v=technet.10)
