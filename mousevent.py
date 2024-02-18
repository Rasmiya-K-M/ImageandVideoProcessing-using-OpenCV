import cv2

def drawCircle(event,x,y,flas,param):
    if event==cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(image,(x,y),10,(255,0,0),-1)
image=cv2.imread('tj.jpg',1)
cv2.namedWindow('image')
cv2.setMouseCallback('image',drawCircle)
while 1:
    cv2.imshow('image',image)
    if cv2.waitKey(20) & 0xFF==ord('q'):
        break
cv2.destroyAllWindows()
