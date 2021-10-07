import cv2
import os
 
for root, subdirs, files in os.walk('back'):
    for f in files:
        if f.endswith('jpg'):
            # print(f)
            img = cv2.imread('back/' + f)
            img = cv2.resize(img, (640, 480))
            cv2.imwrite('back_resize/'+f, img)
            print(*["Image", f, "is resized to 640 X 480"])
