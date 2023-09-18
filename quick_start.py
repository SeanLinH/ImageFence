import os 
import cv2
import numpy as np
from tqdm import tqdm


pts = open('points.txt', 'r', newline='\n').readlines()
pts = np.array(list(map(lambda x: x.strip('\n').split(','), pts))).astype('int32')
center = pts.mean(axis=0).astype('int32')
para = []
formula = []
for i in range(len(pts))[::-1]:
    x1 = pts[i][0]
    y1 = pts[i][1]
    x2 = pts[i-1][0]
    y2 = pts[i-1][1]
    slope =  (y2 - y1) /  (x2-x1) 
    b =  y1 - slope * x1
    para.append([slope, b])

for i in range(len(para)):
    if (center[1] - (para[i][0] * center[0] + para[i][1])) > 0:
        formula.append([1,para[i][0], para[i][1]])
    else:
        formula.append([2,para[i][0], para[i][1]])
        

        
def fence(x, y, formula):
    ans = []
    def mode(n, slope, b):
        if n ==1:
            return y - (slope * x + b)
        elif n == 2:
            return slope * x + b -y
    for cal in formula:
        ans.append(mode(cal[0],cal[1],cal[2]))
    
    if False not in [x>0 for x in ans]:
        return True
    return False


def save_mask(image):
    '''Generate a mask matrix and only have 0 & 1. If you use the ImageFence tool,
    you will get an archive that will have anchors points.'''
    mask = np.zeros(image.shape,dtype='uint8')
    for i in tqdm(range(img.shape[1])):
        for j in range(img.shape[0]):
            if fence(i, j, formula):
                cv2.circle(mask, (i,j), 1, [1,1,1],-1)
    np.save('output/mask.npy', mask)

img = cv2.imread('123.jpg')  ## 測試影像的檔名
for i in range(img.shape[1]):
    for j in range(img.shape[0]):
        if fence(i,j,formula):
            cv2.circle(img, (i,j), 1, (0,0,255), -1)

cv2.imwrite('output/fence_img.jpg', img)
save_mask(img)
