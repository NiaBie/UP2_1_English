# single in rand, repeat the wrong 
import functools,sys,logging,random,codecs,time,os
from collections import Iterable,Iterator

def array(row,line=0,num=0):
  if line==0:
    return [num for i in range(row)]
  return [[num]*line for i in range(row)]

def exchange(words, problem):
  len_t = len(words) - 1
  for i in range(1000):
    u = random.randint(0, len_t)
    v = random.randint(0, len_t)
    words_t = words[u]
    words[u] = words[v]
    words[v] = words_t
    words_t = problem[u]
    problem[u] = problem[v]
    problem[v] = words_t

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
wrong_time = words[:]
for i in range(length):
  wrong_time[i] = 0
exchange(words, problem)
head = 0
tail = length - 1
num_last = -1
print('total words:',length)
print("\033[34;1mS is for skip!\033[0m")
# test
while head < length:
  j = random.randint(head, tail)
  if (j == num_last):
    j = random.randint(head, tail)
  k = 0
  temp=len(words[j])-1
  str=input(problem[j])+'\n'
  if not(str==words[j] or str=='S\n'):
    while not(str==words[j] or str=='S\n'):
      wrong_time[j] += 1
      if k<temp:
        #k+=1
        k=temp
      for l in range(k):
        print(words[j][l],end='')
      print()
      str=input(problem[j])+'\n'
    if (str == 'S\n'):
      temp = words[j]
      words[j] = words[head]
      words[head] = temp
      temp = problem[j]
      problem[j] = problem[head]
      problem[head] = temp
      temp = wrong_time[j]
      wrong_time[j] = wrong_time[head]
      wrong_time[head] = temp
      head += 1
      print('next!')
      num_last = -1
    else:
      print('next-')
      num_last = j
  else:
    temp = words[j]
    words[j] = words[head]
    words[head] = temp
    temp = problem[j]
    problem[j] = problem[head]
    problem[head] = temp
    temp = wrong_time[j]
    wrong_time[j] = wrong_time[head]
    wrong_time[head] = temp
    head += 1
    print('next!')
    num_last = -1
  print("\033[32m%s\033[0m" % (words[j][:(len(words[j]) - 1)]))
# display
for i in range(length):
  if wrong_time[i] != 0:
    print("\033[32m%s\033[34;1m%-20s\033[31;1m%10d\033[0m" % (problem[i], words[i][:(len(words[i]) - 1)], wrong_time[i]))
