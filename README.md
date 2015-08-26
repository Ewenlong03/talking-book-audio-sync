## 如何使用Long Audio Aligner

```shell
$ git clone git@github.com:li2/TalkingBook21_AudioSync.git
$ cd aligner
$ python align-wav-txt.py demo/Unsigned8bitFormat.wav demo/raw.txt 
Running ant
Updating batch
Aligning text
Transcription: pumas are large catlike animals which are found in americawhen reports came into london zoo......

# --------------- Summary statistics ---------
   Total Time Audio: 112.00s  Proc: 3.28s  Speed: 0.03 X real time
<unk>(0.0,0.49) are(1.88,1.91) large(2.07,2.31) animals(2.34,2.94) which(2.94,3.15) are(3.15,3.29) found(3.29,3.67) in(3.67,3.76) americawhen(3.76,4.39) reports(5.22,5.92) came(5.92,6.3) into(6.33,6.66) london(6.66,7.09) zoo(7.09,7.42)......

# you can also execute:
$ python align-mp3-txt.py demo/OtherFormat.mp3 demo/raw.txt
```

这是一个命令行工具，它最终执行的是`jar -jar bin/aligner.jar your/audio/file your/txt/file`，python脚本`align-wav-txt.py`在其基础上做了一层封装。

这里需要特别强调的是，**aligner对音频文件特别挑剔**，遇到过的**问题之一：耗尽计算机CPU，甚至超频，最后java内存溢出**。

```shell
PID    COMMAND      %CPU  TIME     #TH   #WQ  #PORT MEM    PURG   CMPRS  PGRP  PPID  STATE    BOOSTS
17203  java         718.4 64:34.94 30/8  0    95    4276M- 0B     51M    17203 15729 running  *0[7]

$ ps aux | grep 17203
weiyi           17203 658.3 26.2  8298480 4392764 s000  R+   10:07上午  76:11.30 /usr/bin/java -jar bin/aligner.jar ../demo.wav ../demo.txt
Exception in thread "main" java.lang.OutOfMemoryError: GC overhead limit exceeded
at edu.cmu.sphinx.decoder.search.AlignerSearchManager.collectSuccessorTokens(AlignerSearchManager.java:584)
```

**问题二：只能同步一小部分文本**。
下面是我对网上下载的新概念英语3做的测试：

```shell
(章节号)  同步文本的时长/总时长
01  123/129
02  115/122
03  129/136
07  81/129
08  74/136
09  17/146
10  6/150
12  117/130
13  44/123
04,05,06,11,14,15,16,17,19,20,21,22,24,27    Exception in thread "main" java.lang.ArrayIndexOutOfBoundsException
18  54/140
23  171/178
25  0~100缺失
26  144/190
```

这两个问题应该都和音频格式有关。音频编辑软件**audacity**可以导出音频为不同的格式，经过对比测试时发现，在导出对话框的format选项中，选择**“其它非压缩音频文件：文件头WAV(Microsoft), 编码Unsigned 8 bit PCM”**，这种音频格式能够得到最佳的结果。
![在这里插入图片](https://github.com/li2/TalkingBook21_AudioSync/blob/master/export_as_wav_unsigned8bit.png)

所以我在demo文件夹里上传了两种格式的音频文件，用以对比。

[参考I am not sure if this will be of any help to you, but I tried different audio formats as input with surprising results.](http://sourceforge.net/p/cmusphinx/discussion/sphinx4/thread/9ac8582e/)

### google 关键字
audio text alignment, audio text sync

### aligner 依赖环境
Python 2.7, java, ant, sox,

如果你在执行脚本的过程中，遇到错误，需要根据错误提示搜索原因并安装相关包，比如ubuntu12.04环境下执行align-mp3-txt.py时，提示错误：

> no handler for file extension `mp3'

需要安装`libsox-fmt-mp3`


## 处理Long Audio Aligner生成的Timing File

### 插入缺失的文本和标点符号

细心的你可能已经发现aligner生成的timing file实际上是根据音频文件转译的文本，**与原始文本相比：无标点符号（包括段落分隔符）；错字（youre, dont, isnt之类缺失`'`）；漏字**，等等。

于是我写了一个python脚本`parse_timing_json.py`，它比较原文和aligner输出的json文件，把原文未被识别的文本插入到json文件中，得到**一个包含完整文本和时间的json文件**.
但是，这个脚本容错性非常不好，或者说，对输入文件非常挑剔，输入json文件漏字不能太多，和txt文件必须几乎一致，这个脚本才可以把时间戳和原文做匹配。 幸运的是，long-audio-align产生的json文件可以满足。

### 处理换行符和超过行宽的字符串

如果json文件中的字符串包含换行符，则以换行符为界拆分字符串，换行符单独拿出来。目的是方便app处理换行：app读取到换行符后，使其占据整个linearlayout，使app所显示的文本段落结构更加清晰。
另外，如果字符串包含的字符个数超过5个，则拆分这个字符串。

```shell
# 如果你能正确执行align-wav-txt.py，那么你会在demo文件夹中得到一个名为raw.json的文件（一定要使用align-wav-txt.py参生的完整的json文件）：
$ cd parse_timing_json/
$ python parse_timing_json.py ../aligner/demo/raw.json ../aligner/demo/raw.txt
# 生成文件raw.json.out.json，

$ python parse_new_line.py ../aligner/demo/raw.json.out.json
# 生成文件raw.json.out.json.out.json

```

对比处理前后的json文件：

```html
处理前：
 ["are", 1.88, 1.91], ["large", 2.07, 2.31], ["animals", 2.34, 2.94], ["which", 2.94, 3.15], ["are", 3.15, 3.29], ["found", 3.29, 3.67], ["in", 3.67, 3.76], ["americawhen", 3.76, 4.39], ["reports", 5.22, 5.92],
 
处理后：
["are", 2.07], ["large", 2.07], [", cat- like animals", 2.34], ["which", 2.94], ["are", 3.15], ["found", 3.29], ["in", 3.67], ["America. When reports", 5.22],
```


Audio Sync Tools
======================

## Aligner Using SMU Sphinx

In the folder `aligner`, you'll find code - all based on Weston Ruter's work - that attempts to download
SMU Sphinx, then do some work to sync files. The Gettysberg address file is the easist to work with.

## JavaScript Library

In the folder 'demo', you'll find the aligner code with several examples. The file `dream.html` aligns to inpage HTML, while
`esvbible-local.html` aligns to HTML loaded via AJAX.

Dependencies
------------

* Python 2.7
* java
* ant
* [sox](http://sox.sourceforge.net/)
* svn

License
-------
Dual licensed under the MIT or GPL Version 2 licenses.  
MIT License: http://creativecommons.org/licenses/MIT/  
GPL 2.0 license: http://creativecommons.org/licenses/GPL/2.0/
