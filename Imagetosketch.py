print('Hello World')
import cv2 
image=cv2.imread(r'C:\Users\kushm\Downloads\image (5).png')
greyimg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(greyimg, (11,11), 0)
invertedblur = cv2.bitwise_not(blur)
sketch = cv2.divide(greyimg, blur, scale=240.0)
cv2.imwrite("sketch.png", sketch) 
img=cv2.imread(r'C:\Users\kushm\.vscode\sketch.png')
cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindoWS