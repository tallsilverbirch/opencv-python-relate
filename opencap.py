import cv2
 
cap = cv2.VideoCapture(0)

cap.set(3,680)
cap.set(4,480)
print("width={}".format(cap.get(3)))
print("height={}".format(cap.get(4)))
if cap.isOpened():
    while True:
        success, img = cap.read()
        img = cv2.resize(img, (1280, 740), interpolation=cv2.INTER_LINEAR)
        print(img.shape)
        cv2.imshow("Image", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
