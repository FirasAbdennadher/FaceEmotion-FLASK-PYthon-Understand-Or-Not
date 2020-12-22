import cv2
# Playing video from file:
cap = cv2.VideoCapture('C:/Users/LENOVO/ala/new_dataset/fehem/WIN_20200525_04_36_10_Pro.mp4')

currentFrame = 0
while(True):
       # Capture frame-by-frame
       ret, frame = cap.read()

       if not frame is None:
           # Saves image of the current frame in jpg file
           name = 'C:/Users/LENOVO/ala/new_dataset/f/l' + str(currentFrame) + '.jpg'
           print ('Creating...' + name)
           cv2.imwrite(name, frame)
           #cv2.imshow(name, frame)
       else:
           break

       # To stop duplicate images
       currentFrame += 1

# When everything don e, release the capture
cap.release()
cv2.destroyAllWindows()





import os
dirname= "E:/Téléchargements/vidéo_pfa/dataset/img_mouch_fehem_grey48"
k=260
if os.path.isdir(dirname):
    for i, filename in enumerate(os.listdir(dirname)):
        print(dirname + "/" + filename)
        os.rename(dirname + "/" + filename, dirname + "/" + str(k) + ".jpg")
        k+=1
        
        
        

        

from PIL import Image
for k in range(334):
    img = Image.open('E:/img_mouch_fehem_grey/'+str(k)+'.jpg')
    img = img.resize((48,48), Image.ANTIALIAS)
    img.save('E:/img_mouch_fehem_grey48/'+str(k)+'.jpg') 





   
    
    
    
    
import cv2
for k in range(309):  
    image = cv2.imread('C:/Users/LENOVO/img_fehem48/'+str(k)+'.jpg')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('C:/Users/LENOVO/img_fehem_grey/'+str(k)+'.jpg',gray)

    
from PIL import Image    
im = Image.open('C:/Users/LENOVO/Downloads/vidéo_pfa/image_fehem/extraction_img_fehem/0.jpg').convert('L')
im = im.crop((1, 1, 500, 200))
im.save('C:/Users/LENOVO/Downloads/vidéo_pfa/image_fehem/extraction_img_fehem/_0.jpg')

    
import cv2
img = cv2.imread("0.png")
crop_img = img[10:50+20, 100:30+100]
cv2.imshow("cropped", crop_img)
cv2.waitKey(0)    
    
    
    
    


