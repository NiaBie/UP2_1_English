import functools,sys,logging,random,codecs
from collections import Iterable,Iterator
from types import MethodType,FunctionType
from enum import Enum

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
  file=codecs.open(name+'_p','r',encoding='utf-8')
  problem+=file.readlines()
  name=input('输入文件名(s for end):')
length=len(words)
print('总单词数为:',length)
for i in range(length):
  k=0
  temp=len(words[i])-1
  str=''
  while not(str==words[i] or str=='s\n'):
    str=input(problem[i])+'\n'
    if k<temp:
      #k+=1
      k=temp
    if str!=words[i]:
      for l in range(k):
        print(words[i][l],end='')
      print()
  print('next!')
print('finish!')
