# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 10:23:54 2022

@author: admin

设计思路
文本和音频的文件路径获取，并读取所有的文本内容和所有的音频文件信息，存入对应的列表中
增加参数和其他数值的获取方式，灵活修改对应的音频文件名，并对音频文件名列表的修改、排序
按照预期格式对文本内容和对应的音频文件名进行连接，注意处理数据格式以便能正确输出预期的排版格式
写入新文件
"""

import os
import argparse

from datetime import datetime

parser = argparse.ArgumentParser()

parser.add_argument('--title', type=str,default='SSB')
parser.add_argument('--rmtitle', type=str,default='新录音 ')
parser.add_argument('--test', type=str,required=True,help='test with require value')
args = parser.parse_args()

def textInfo():
    with open('text.txt','r',encoding='utf-8') as textfile:
        for  line in textfile:
            listOfLines.append(line.strip())

        
    setNewName()


def modifyOldName(num,name):
    title_data = datetime.now().year

    file_type=os.path.splitext(name)[-1]

    title=args.title+str(title_data)
    new_title=title+str(num).zfill(3)
    name=new_title
        

    return name,file_type


def setNewName():
    for i in files:
        oldname=i
        num=files.index(i)
        newname,file_type=modifyOldName(num,oldname)
        #line=i+" "+j
        #newLines.append(line)
        #info=info.join([newname+' ',info])

        os.rename(work+os.sep +oldname,work+os.sep +newname+file_type)
        wavlist.append(newname.replace('.wav',' '))
    wavlist.sort(key= lambda x:int(x[3:-1]))  
    print(wavlist)
    modifyText()


def modifyText():
    with open('newtext.txt','w',encoding='utf-8') as newtextfile:
        print(len(wavlist))
        for  j in range( len(wavlist)):
            #newLines.append([wavlist[j]+'' +listOfLines[j]])
            temp=wavlist[j]+' '+listOfLines[j]
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
 