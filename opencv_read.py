import cv2
#读取图片
img=cv2.imread(“图片所在路径”, cv2.IMREAD_COLOR)

#在屏幕上长时间显示图片
cv2.imshow('图片名字',img)
cv2.waitKey(0)

#保存图片
cv2.imwrite ('图片名字.png',img)

