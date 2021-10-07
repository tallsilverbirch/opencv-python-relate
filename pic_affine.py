#图像旋转
import numpy as np
import cv2
#读取图片
img = cv2.imread(“图片名称，包含完整路径”)
#仿射变换矩阵
M=np.array([[0,0.5,-10],[0.5,0,0]])
#旋转图片
#通过affine
img1=cv2.warpAffine(img,M, (750,750))
#显示图片
cv2.imshow("图片旋转", img1)
cv2.waitKey(0)
