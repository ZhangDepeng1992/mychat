#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 17:44:33 2018

@author: tyou
"""

import sys
import os
import MeCab







def read_corpus(filename):
    
    a = open(filename,'r')
    for aline in a.readlines():
 
        if aline.startswith('＠'):
            continue
        if aline.find('：')  >= 0 :
            aline = aline[aline.find('：') + 1:]
  
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

def make_word(input_str):
    wakatext = input_str
    m = MeCab.Tagger('-Owakati')
    return m.parse(wakatext)

def write_corpus(filename):
    import random
    str_ = ''
    a = open(filename,'w',1)
    m = 0
    for n in range(len(alist)):
       # print(alist[n])
        str_ = ''
        str_ = make_word(alist[n])
        str_ = str_.strip()
        str_ = str_.replace(' ','/')
        #if str_ == '':
        #    pass
        #for b in alist[n] :
        #    str_ = str_ + b + '/'
        if m < random.randint(3,8) :
            a.write('M ' + str_  + '\n')
            m = m + 1
        else :
            a.write('M ' + str_  + '\n')
            a.write('E ' + '\n')
            m = 0
        if n == len(alist) - 1:
            a.write('E ' + '\n')
    a.close





if __name__ == "__main__":
    files_path = './nucc'

    filenames = os.listdir(files_path)

    
    alist = []
    for file_ in filenames:
         
        filename = os.path.join(files_path , file_)
        #print (filename)
        read_corpus(filename)
    
        #write_corpus(file_)
        #print(alist)
    write_corpus('1.txt')
    
    
'''
for filename in filenames:
    print(filename)

a = open(files_path + '/data001.txt','r')
for aline in a.readlines():
    print(aline)
    '''
