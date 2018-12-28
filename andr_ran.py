# -*- coding: utf-8 -*- 
import functools,sys,logging,random,codecs
from collections import Iterable,Iterator

def array(row,line=0,num=0):
	if line==0:
		return [num for i in range(row)]
	return [[num]*line for i in range(row)]

words=[]
problem=[]
name=input('输入文件名(s for end):')
file=open(name,'r')
while name!='s':
	file=open(name,'r')
	words+=file.readlines()
	file=codecs.open(name+'_cp','r',encoding='utf-8')
	problem+=file.readlines()
	name=input('输入文件名(s for end):')
length=len(words)
print('总单词数为:',length)
times=length*4
print('一共%d次'%(times))
#times=input('输入次数:')
#times=int(times)
#head=input('输入开始(1开始):')
#tail=input('输入结束:')
#head=int(head)
#tail=int(tail)
head=1
tail=length
print('s for skip!')
for i in range(times):
	j=random.randint(head-1,tail-1)
	k=0
	temp=len(words[j])-1
	str=''
	while not(str==words[j] or str=='s\n'):
		str=input(problem[j])+'\n'
		if k<temp:
		#	k+=1
			k=temp
		if str!=words[j]:
			for l in range(k):
				print(words[j][l],end='')
			print()
	print('next!')
print('finish!')
