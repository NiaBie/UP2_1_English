import functools,sys,logging,random,codecs,os
from collections import Iterable,Iterator
from types import MethodType,FunctionType
from enum import Enum

def array(row,line=0,num=0):
  if line==0:
    return [num for i in range(row)]
  return [[num]*line for i in range(row)]

def exchange(words, problem):
  len_t = len(words) - 1
  print(len_t)
  for i in range(1000):
    u = random.randint(0, len_t)
    v = random.randint(0, len_t)
    words_t = words[u]
    words[u] = words[v]
    words[v] = words_t
    words_t = problem[u]
    problem[u] = problem[v]
    problem[v] = words_t

def pf_all(words):
  print('------------------------------------------')
  for i in words:
    print(i, end = '')
  print('------------------------------------------')

words=[]
problem=[]
suffix = input('problem suffix:')
num_start=int(input('start file ord:'))
num_end=int(input('end file ord:'))
while num_start <= num_end:
  num_part = 1
  name = ("%d_%d" % (num_start, num_part))
  # print(name)
  while (os.access(name, os.F_OK) == True):
    print("add %s" % name)
    file=open(name,'r')
    words+=file.readlines()
    file=codecs.open(name+suffix,'r',encoding='utf-8')
    problem+=file.readlines()
    num_part += 1
    name = ("%d_%d" % (num_start, num_part))
  num_start += 1
length=len(words)
# print(len(words))
# pf_all(words)
exchange(words, problem)
# pf_all(words)
print('total words:',length)
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
