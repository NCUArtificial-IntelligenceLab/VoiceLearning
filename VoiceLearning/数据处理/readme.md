# 数据处理任务
## 任务类型：对音频文件和音频文本进行处理
### Task001

#### 文件夹结构

	├──RenameOrder.py
	├──text.txt
	├──wav
#### 说明
从路径```\\DESKTOP-4NCNNIN\ls\TaskList\WavTest.zip```复制并按照文件夹结构解压提取对应的文件夹，后执行示例脚本```RenameOrder.py```，在执行后wav文件夹内的音频文件将根据要求删除原始文件名中的汉字部分，并且根据```text.txt```的文本内容和```wav```下的音频顺序，创建新的文本```newtext.txt```。其中```newtext.txt```的格式将转变为

	无文件类型后缀的音频文件名+空格字符+音频文件对应的文本行


#### 要求
- 修改文件重命名方式，在保证原排序的基础上将文件命名为英文字符+数字字符递增的结构。具体命名结构可参考[issues](https://github.com/HuiGulab/VoiceLearning/issues/3)内MFA提取的音频文件名格式