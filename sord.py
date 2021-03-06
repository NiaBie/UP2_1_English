# single in rand, display wrongtimes
import functools,sys,logging,random,codecs,time
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

def pf_all(words):
  print('------------------------------------------')
  for i in words:
    print(i, end = '')
  print('------------------------------------------')

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
length = len(words)
wrong_time = words[:]
for i in range(length):
  wrong_time[i] = 0
#times=input('输入次数:')
#times=int(times)
#head=input('输入开始(1开始):')
#tail=input('输入结束:')
#head=int(head)
#tail=int(tail)
exchange(words, problem)
head = 1
tail = length
print('total words:',length)
# tm_year, tm_mon, tm_mday, tm_hour, tm_min, tm_sec
total_score = 0
start_time = time.localtime()
start_score = (start_time[3]*60 + start_time[4])*60 + start_time[5]
for i in range(length):
  k = 0
  temp=len(words[i])-1
  str=''
  wrong_time[i] -= 1
  while not(str==words[i] or str=='s\n'):
    wrong_time[i] += 1
    str=input(problem[i])+'\n'
    if k<temp:
      #k+=1
      k=temp
    if str!=words[i]:
      for l in range(k):
        print(words[i][l],end='')
      print()
  total_score = total_score + 100
  print('next!')
end_time = time.localtime()
end_score = (end_time[3]*60 + end_time[4])*60 + end_time[5]
for i in range(length):
  if wrong_time[i] != 0:
    print("%s:%d" % (words[i][:len(words[i]) - 1], wrong_time[i]))
