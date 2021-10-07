#图像旋转
import numpy as np
import cv2
#读取图片
img = cv2.imread(“图片名称，包含完整路径”)
#旋转图片
img1=cv2.getRotationMatrix2D (（0，0），90，1)
#显示图片
cv2.imshow("图片旋转", img1)
cv2.waitKey(0)
