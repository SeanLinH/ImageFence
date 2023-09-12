import os
import cv2
import matplotlib.pyplot as plt
import numpy as np


pts = open('points-5.txt', 'r', newline='\n').readlines()

p = ['e','d','c','b','a']
for i in range(len(pts))[::-1]:
    x1 = int(pts[i].split(',')[0].strip('\n'))
    y1 = int(pts[i].split(',')[1].strip('\n'))
    x2 = int(pts[i-1].split(',')[0].strip('\n'))
    y2 = int(pts[i-1].split(',')[1].strip('\n'))
    if x2 > x1:
        slope = (y2 - y1)/ (x2-x1)
        b =  y1 - slope * x1
    else:
        print('down')
        slope = - (y2 - y1)/ (x2-x1)
        b =  slope * x1 - y1
    print(f'{p[i]} = y - int({slope} * x + {b}) ')



def fence(x, y):
    a = int(1.1953488372093024 * x + -382.22325581395353) - y
    b = int(-0.10714285714285714 * x + 619.3928571428571) - y
    c = int(1.2011834319526626 * x + -276.81065088757396) - y
    d = int(-17.333333333333332 * x + 9287.0) - y
    e = int(-0.3142857142857143 * x + 454.1142857142857) - y
    if a>0 and b>0 and c>0 and d>0 and e>0:
        return True
    return False


img = cv2.imread('123.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
for i in range(1000):
    for j in range(1000):
        if fence(i,j):
            cv2.circle(img, (i,j), 1, (255,0,0), -1)
plt.imshow(img)

