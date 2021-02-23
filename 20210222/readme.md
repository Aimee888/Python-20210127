# 反编译exe  
链接：https://www.cnblogs.com/smart-zihan/p/14434498.html
参考链接：https://blog.csdn.net/qq_44198436/article/details/97314626?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task  

第一步：自己写一个py文件打包成exe  
~~~
tartget_exe.py ->target_exe.exe
pyinstaller -F target_exe.py

rename target_exe.py->target_exe_origin.py
~~~
第二步：下载pyinstxtractor.py（百度上搜名字可以找到）
~~~  
1. 将下载好的pyinstxtractor.py放在与exe同级目录下  
2. 在cmd窗口下运行python pyinstxtractor.py target_exe.exe，解压后会生成target_exe.exe_extracted的文件夹  
~~~
第三步：下载反编译工具uncompyle6: pip install uncompyle6  https://www.cnblogs.com/pcat/p/11625300.html  
下载16进制编辑器（网上直接搜也可以找到）：https://www.jb51.net/softs/557257.html#downintro2
~~~
1. 在target_exe.exe_extracted找到没有后缀名的struct和target_exe文件
(target_exe就是我们最后要反编译的pyc文件)
2. 用16进制编辑器打开strcut和target_exe，发现target_exe的首位是E3，
而struct的0C位是E3，我们知道前面的字节代表Python的版本和时间戳，
生成pyc的时候会把它去掉，那么我们反编译就需要将它补齐。所以将struct E3
前面的字节copy到target_exe中，并且将target_exe添加后缀.pyc
3. 反编译target_exe.pyc -> uncompyle6 -o target_exe.py target_exe.pyc
4. 将得到的target_exe.py和之前的target_exe_origin.py进行对比
5. 通过对比可以看到注释没有了，双引号都变成了单引号，if-and句式变成了两个if，
不过语法没变
~~~