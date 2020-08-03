# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 15:04:42 2020

@author: AE401
"""

weight=float(input("請輸入體重(Kg)"))
height=float(input("請輸入身高(cm)"))
height=height/100
Bmi=weight//height**2
if Bmi<18.5:
    print("體重不足")
elif Bmi<24:
    print("正常")
elif Bmi<27:
    print("輕度肥胖")
elif Bmi<30:
    print("中度肥胖")
elif Bmi<35:
    print("過重")
else:
    print("重度肥胖")