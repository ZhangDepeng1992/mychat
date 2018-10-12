#-*- coding:utf-8 -*- 
alist = [] 
a = open('./nucc/data001.txt','r')
for aline in a.readlines():
  #  print(aline)
  '''
  if aline.startswith('F'):
      aline = aline[5:]
  if aline.startswith('M'):
      aline = aline[5:]
  if aline.startswith('Ｘ'):
      aline = aline[2:]
  '''
  if aline.startswith('＠'):
      continue
  if aline.find('：')  >= 0 :
      aline = aline[aline.find('：') + 1:]
  #aline = aline.strip('＜笑い＞')
  if aline.find('（') >= 0 :
      aline = aline[:aline.find('（')] + aline[aline.find('）') + 1 :]
  if aline.find('＜') >= 0 :
      aline = aline[:aline.find('＜')] + aline[aline.find('＞') + 1 :]
  aline = aline.strip()
  if aline == '':
      pass
  else:
      alist.append(aline)
a.close
#print(alist)

import random
str_ = ''
a = open('corpus001.txt','w',1)
m = 0
for n in range(len(alist)):
    print(alist[n])
    str_ = ''
    for b in alist[n] :
        str_ = str_ + b + '/'
    if m < random.randint(3,8) :
        a.write('M ' + str_  + '\n')
        m = m + 1
    else :
        a.write('M ' + str_  + '\n')
        a.write('E ' + '\n')
        m = 0
    if n == len(alist) - 1:
        a.write('E ' + '\n')
    #a.write('M ' + alist[n] + '\n')
a.close
