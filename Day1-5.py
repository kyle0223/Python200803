# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 14:29:14 2020

@author: AE401
"""

score=input("輸入成績")
score=int(score)

if score>=0 and score<=100:
    if score>=90 and score<100:
        print("A")
    elif score>=80 and score<90:
        print("B")
    elif score>=70 and score<80:
        print("C")
    elif score>=60 and score<70:
        print("D")
    elif score>=50 and score<60:
        print("E")
    elif score>=40 and score<50:
        print("F")
    elif score>=30 and score<40:
        print("G")
    elif score>=20 and score<30:
        print("H")
    elif score>=10 and score<20:
        print("I")
    else:
        print("J")
else:
    print("請重新輸入")