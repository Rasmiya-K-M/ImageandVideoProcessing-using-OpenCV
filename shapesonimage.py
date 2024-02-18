import cv2
image=cv2.imread('tj.jpg',1)
cv2.line(image,(0,0),(155,286),(255,0,0),5)
cv2.rectangle(image,(162,160),(30,90),(0,300,0),5)
cv2.circle(image,(10,10),10,(0,0,255),-1)
cv2.circle(image,(157,10),10,(0,0,255),-1)
cv2.circle(image,(10,286),10,(0,0,255),-1)
cv2.circle(image,(157,286),10,(0,0,255),-1)
font=cv2.FONT_HERSHEY_DUPLEX
cv2.putText(image,'HI',(70,135),font,1,(0,255,255))
cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
