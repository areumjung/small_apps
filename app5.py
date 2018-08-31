import cv2
import glob, os

os.chdir('/Users/areum/Documents/python_app/image/sample-images')


images=glob.glob("*.jpg")

for image in images:
    img=cv2.imread(image,0)
    re=cv2.resize(img,(100,100))
    cv2.imshow("Hey",re)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()
    cv2.imwrite("resized_"+image,re)
