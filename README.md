# JsonToSRTCaption
本程序可实现json批量转srt并翻译
srt转json
srt英文字幕转srt中文字幕

各个文件的说明
=============
### main.py
主菜单

### translator.py
翻译模块使用方法：import后，调用 `translator.translate(翻译内容字符串)`  
这个代码是网上搬的，改良为发送翻译内容前特殊符号转义成url规定的格式（因为这样就不会出现奇奇怪怪的问题了）。翻译语言默认是英文转中文。可以修改这个里面的翻译from...=参数。可以设置为"auto"自动判断语言，不过我一般用eng。

！谷歌翻译是不要超过5000字，超过请分段。调用前请检查字数。英文的话我建议保守4500。其他外文的话因为转义了发送的东西会多得多要向下折减。我试过日文的1000字是可以的，不会超过限制。  

### convert.py    
将给定路径的所有json且不存在对应srt文件的json文件会转换成对应的srt文件。  
如果 **不包含** 中文的话还会翻译（所以日文会比较扯，但目前还不太有时间做得太细）。  
目前还局限在英文，其他用的不多。  
如果有用到其他语言翻译的话，调用的时候改一下translator的参数。  

### SrtToJson
如其名

### sample.json 
是一个栗子~

### translateApi.json
填写百度翻译api信息

食用说明
========
申请百度翻译api标准版（免费，限制一秒一次）

地址：[点击此处](http://api.fanyi.baidu.com/api/trans/product/apichoose)

将api信息填入translateApi.json。参见translateApi_sample.json。

终端输入： `python -u mian.py`  
有时输出多了会攒一段时间等缓存满了再输出。这就会造成输出不及时，没有反馈。
-u 表示不缓存直接输出。

这里再多缩一句windows自带终端不支持我代码里的颜色输出，一些输出看起来会非常奇怪。  
所以建议使用linux终端，或在windows下使用一些高级终端。  
微软的windows terminal就很不错！

许可声明
========
GPL许可。欢迎Star 或 fork (●ˇ∀ˇ●)