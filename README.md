# JsonToSRTCaption
本程序可实现
* 「特定的」json字幕批量转srt并翻译（详见sample.json）
* srt转json
* srt英文字幕转srt中文字幕

注：输入的英文srt必须是单行字幕，因程序采用隔行读取的方法。
且注意srt末尾不要有多余的空行。

其它格式的json需要自行修改源代码。
json的读入目前还比较粗暴。但是目前还没时间换成json库。

各个文件的说明
=============
### main.py
主菜单

### translator.py
翻译模块使用方法：import后，调用 `translator.translate(翻译内容字符串)`  

翻译模块使用百度翻译。

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

注意，百度翻译现在需要实名认证才能具有较高的可用度。[权益说明](http://api.fanyi.baidu.com/doc/8)
请实名认证后切换为高级版，否则需要修改程序convert中的判断阈值（标准版为1000字符每次请求）。

将api信息[管理百度翻译API](http://api.fanyi.baidu.com/api/trans/product/desktop)填入translateApi.json。参见translateApi_sample.json。

终端输入： `python -u mian.py`  
有时输出多了会攒一段时间等缓存满了再输出。这就会造成输出不及时，没有反馈。
-u 表示不缓存直接输出。

这里再多缩一句windows自带终端不支持我代码里的颜色输出，一些输出看起来会非常奇怪。  
所以建议使用linux终端，或在windows下使用一些高级终端。  
微软的windows terminal就很不错！

许可声明
========
GPL许可。欢迎Star 或 fork (●ˇ∀ˇ●)
