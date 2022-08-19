# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 10:23:54 2022

@author: admin

设计思路
文本和音频的文件路径获取，并读取所有的文本内容和所有的音频文件信息，存入对应的列表中
修改对应的音频文件名，并对音频文件名列表的修改、排序
按照预期格式对文本内容和对应的音频文件名进行连接，注意处理数据格式以便能正确输出预期的排版格式
写入新文件
"""

import os


def textInfo():
    with open('text.txt','r',encoding='utf-8') as textfile:
        for  line in textfile:
            listOfLines.append(line.strip())
        print(listOfLines)
        
    setNewName()


def modifyOldName(name):
    rm="新录音 "
    if rm in name:
        name=name.replace(rm,'')

    return name


def setNewName():
    for i in files:
        oldname=i
        newname=modifyOldName(oldname)
        #line=i+" "+j
        #newLines.append(line)
        #info=info.join([newname+' ',info])

        os.rename(work+os.sep +oldname,work+os.sep +newname)
        wavlist.append(newname.replace('.wav',' '))
    wavlist.sort(key= lambda x:int(x[:-1]))  
    print(wavlist)
    modifyText()


def modifyText():
    with open('newtext.txt','w',encoding='utf-8') as newtextfile:
        print(len(wavlist))
        for  j in range( len(wavlist)):
            #newLines.append([wavlist[j]+'' +listOfLines[j]])
            temp=wavlist[j]+''+listOfLines[j]
            newLines.append(''.join(temp))

        #newtext=(' '.join(map(str,newLines)))
        newtext=('\n'.join(newLines))
        newtextfile.write(newtext)


if __name__=='__main__':
    work=os.getcwd()
    if os.path.exists('wav'):
        work=os.path.join(work,'wav')
        print('yse')
    else:
        os.makedirs('wav')
        print('no and copy files to wav fold')
    wavlist=list()

    listOfLines  =  list()
    newLines=list()
    newtext=''

    files=os.listdir(work)
    print('star with main')
    textInfo()
 