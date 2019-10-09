dll劫持原理学习详细笔记（针对基础很薄弱的人）

开发环境：win10 1809 + vs2017 15.9.12





首先写一个stub，文件-》新建-》项目-》左侧栏的已安装-》Visual C++-》Windows 桌面-》Windows 控制台应用程序

vs自动添加的代码不用管，在main()中添加如下代码：
HMODULE h = LoadLibrary("1.dll");
ShowMsg = GetProcAddress(h, "ShowMessage");
ShowMsg();
别忘记添加头#include <windows.h>以及如果main()声明为int,添加return 0;
参考链接：
https://blog.csdn.net/Joliph/article/details/78755387
https://stackoverflow.com/questions/9545732/what-is-hmodule
https://stackoverflow.com/questions/557081/how-do-i-get-the-hmodule-for-the-currently-executing-code/557859#557859
https://blog.csdn.net/wangshubo1989/article/details/53203718
https://www.cnblogs.com/westsoft/p/5936092.html

此时会有2个错误

第一个提示：const char *类型的实参与LPCWSTR类型的形参不兼容
vs工程默认只支持unicode字符集，需要修改字符集，项目-》属性-》常规-》字符集改为“使用多字节字符集”
参考链接：
https://blog.csdn.net/farmwang/article/details/80658429

第二个提示：未定义标识符"ShowMsg"
需要定义一个指向函数的指针类型：typedef void (*SW)()
然后指定ShowMsg为SW型：SW ShowMsg = ...;
但同时也会有一个新问题，GetProcAddress()返回的值跟SW类型不匹配，所以需要强制转换一下：SW ShowMsg = (SW) GetProcAddress...;
参考链接：
https://stackoverflow.com/questions/3982470/what-does-typedef-void-something-mean
编译程序





然后我们写正常被调用的dll文件，文件-》新建-》项目-》左侧栏的已安装-》Visual C++-》Windows 桌面-》动态链接库（DLL）
不编辑Dll1.cpp，打开dllmain.cpp，在case DLL_PROCESS_ATTACH:下面添加如下代码
MessageBox(NULL, "1", "1", MB_OK);
修改字符集
编译程序
将编译好的ConsoleApplication1.exe和Dll1.dll放到新建的目录test下，将Dll1.dll重命名为1.dll，执行ConsoleApplication1.exe，会弹出一个消息框





然后我们写用于劫持正常dll的dll，也就是伪造的dll，里面有我们想自己实现的代码，我这里只是弹出一个计算器，创建步骤如上
不编辑Dll2.cpp，打开dllmain.cpp，在case DLL_PROCESS_ATTACH下:面添加如下代码：
WinExec("calc.exe", SW_SHOW);
MessageBox(NULL, "1", "1", MB_OK);
修改字符集
编译程序
将编译好的Dll1.dll放到新建的目录test下，重命名为1.dll并删除之前的1.dll文件，再次执行ConsoleApplication1.exe，会弹出一个提示框，同时弹出计算器





dll文件还可以的写法，也是正统的写法：

首先创建一个头文件，添加如下代码：
#ifdef DLL3_EXPORTS // 其实当你创建dll项目时，这个DLL3_EXPORTS是被vs自动定义的宏，名称DLL3是项目名称，其他是固定的
#define DLL3_API __declspec(dllexport)
#else
#define DLL3_API __declspec(dllimport)
#endif

extern "C" DLL3_API void ShowMessage(); // 其实就是声明这个函数是使用c调用标准，然后可用于导出

然后创建一个cpp文件，添加如下代码：
void ShowMessage()
{
	MessageBox(NULL, "1", "1", MB_OK);
}

修改字符集
编译程序

#ifdef 标识符 // 如果标识符被定义，则编译程序段1，否则编译程序段2
程序段1
#else
程序段2
#endif

#ifndef 标识符 // 如果标识符未被定义，则编译程序段1，否则编译程序段2
程序段1
#else
程序段2
#endif

#if 条件 // 如果条件为真（非0），则编译程序段1，否则编译程序段2 
程序段1
#else
程序段2
#endif
以上的#if...都是预编译阶段所做的处理

#pragma once // vs2017起，一般在头文件（.h文件）中自带，旧的编译器不支持，只能用于整个文件
#ifndef 标识符 // 是c/c++标准，编译器都支持，可用于指定代码段
都是用于防止预编译指令#include造成二义性
参考链接：
https://www.cnblogs.com/yanwei-wang/p/8073114.html
https://blog.csdn.net/cv_jason/article/details/81842710

extern "C" // 表明以c语言调用约定（c calling convention）为了让它能够被更多的语言调用
__declspec(dllexport) // 通常用于dll中，要被外部exe使用的函数，变量，类前面
__declspec(dllimport) // 要使用外部的dll时，通常用于exe中，属于隐式调用，像是LoadLibrary好像属于显示调用
隐式调用通常在载入时（load-time）
显示调用通常在运行时（run-time）





调用dll的方式还可以隐式调用，即需要编译后的dll文件以及lib文件，还有编写dll时的头文件，然后
在stub源程序中包含头文件，然后可以直接调用声明的函数，再将dll以及lib文件放到stub的同级目录下
使用时报错，无法打开源文件"Dll3.h"
未完待续。。




参考链接：
https://www.cnblogs.com/carsonzhu/p/5272271.html
https://blog.csdn.net/cstringw/article/details/51981250
https://blog.csdn.net/stone_kingnet/article/details/3862504
https://blog.csdn.net/u010055724/article/details/51538686
https://docs.microsoft.com/en-us/cpp/build/dlls-in-visual-cpp?view=vs-2017
https://docs.microsoft.com/en-us/cpp/build/linking-an-executable-to-a-dll?view=vs-2017
