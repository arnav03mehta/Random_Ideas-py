from funlib import factorial as fac
from itertools import permutations as pm
import numpy as np
import cv2
from funlib import password
key = 0
key = password(key)

if key is True :
    n = 1
    while n < 2:
        dic = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
        print()
        word = str(input('Word : '))
        if word == '.admin' :
            cmd = input('?\ >> ')
            if cmd == 'end' :
                break
            
        l_2 = []
        l = []
        l_3 = ''
        l_4 = []
        for p in range(len(word)):
            l_4.append(word[p])
        if l_4.count('.') == 1 :
            for t in range((l_4.index ('.'))+1,len(l_4)):
                l_3 += l_4[t]
        if l_4.count('.') == 1  :
            for i in range(len(word)-(len(l_3)+1)):
                l.append(word[i])
        else :
            for i in range(len(word)):
                l.append(word[i])
        l.sort() 
        for i in range(len(word)):
            l_2.append(word[i])
        perm = pm(l)
        rank = 0
        total = fac(len(l))
        if l_4.count('.') == 0 :
            for e in list(perm):
                rank += 1
                print(e)
                if list(e) == l_2 :
                    break
            print('rank = ',rank)
            print('total words = ',total)
        else :
            for e in list(perm):
                rank += 1
                print(e)
                if rank == int(l_3) :
                    break
            print('total words = ',total)



