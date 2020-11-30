#!/usr/bin/env python
# coding: utf-8

# In[9]:


import cv2
import sys

img = cv2.imread('./fig1.jpg') # imread로 영상을 불러온다.
if img is None:
    print('Imager load failed!') # 이미지가 없으면 출력
    sys.exit()

cv2.namedWindow('image') 
cv2.imshow('image', img) 
cv2.waitKey()            
cv2.destroyAllWindows() 


# In[10]:


import matplotlib.pyplot as plt
colors = ['b', 'g', 'r']
bgr_planes = cv2.split(img)

for (p, c) in zip(bgr_planes, colors):
    hist = cv2.calcHist([p], [0], None, [256], [0, 256])
    plt.plot(hist, color=c)

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()

plt.show()


# In[28]:


#컬러 히스토그램 평활화
src=img

src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)
ycrcb_planes = cv2.split(src_ycrcb)


# 밝기 성분에 대해서만 히스토그램 평활화 수행
ycrcb_planes[0] = cv2.equalizeHist(ycrcb_planes[0])

dst_ycrcb = cv2.merge(ycrcb_planes)
dst = cv2.cvtColor(dst_ycrcb, cv2.COLOR_YCrCb2BGR)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()


# In[26]:


#샤프닝
sharp=np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
sharp2= np.array([[-1, -1, -1, -1, -1],
                         [-1, 2, 2, 2, -1],
                         [-1, 2, 9, 2, -1],
                         [-1, 2, 2, 2, -1],
                         [-1, -1, -1, -1, -1]]) / 9.0
dst=cv2.filter2D(img,-1,sharp)
dst2=cv2.filter2D(img,-1,sharp2)
cv2.imshow('sharp',dst)
cv2.imshow('sharp2',dst2)
cv2.waitKey()
cv2.destroyAllWindows()


# In[27]:


#평탄한 부분은 가우시안, 엣지는 살리기
#양방향 필터
dst = cv2.bilateralFilter(src, -1, 10, 5)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()

