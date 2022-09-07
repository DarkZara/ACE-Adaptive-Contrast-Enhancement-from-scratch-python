import cv2
import numpy as np

def is_grey_scale(img):
  help='to define type of the image'
    if len(img.shape) < 3:
      return True
    else:
      return False
    
    
def ACE(image, gridSize):
  help='supports rgb and greyscaled images. returns an ACE enhanced image, gets an image and grid size as input'
  
  #to define the grid size
  gh2,gw2=gridSize
  gh=int(gh2/2)
  gw=int(gw2/2)
  #we shall calculate the equalized histogram for each pixel and its naighbours in a certain gridsize
  if is_grey_scale(image):
    #if grey
    #zero padding the image
    ih,iw=image.shape
    padded_image=np.zeros((ih+gh2,iw+gw2), dtype=np.uint8)
    padded_image[gh:ih+gh,gw:iw+gw]=image[:,:]
    
    #enhancing using equalize hist
    for (h,w),pix in np.ndenumerate(image):
        image[h][w]=cv2.equalizeHist(padded_image[h:gh2+h+1,w:gw2+w+1])[gh+1][gw+1]
        
    image=cv2.cvtColor(image,0)
    
  else:
    #if colored
    #zero padding the image
    ih,iw,c=image.shape
    padded_image=np.zeros((ih+gh2,iw+gw2,3),dtype=np.uint8)
    padded_image[gh:ih+gh,gw:iw+gw,:]=image[:,:,:]
    
    #convert to hsv
    padded_image=cv2.cvtColor(padded_image,cv2.COLOR_BGR2HSV)
    img=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    
    #enhancing using equalize hist for channel V
    for (h,w),pix in np.ndenumerate(img[:,:,2]):
      img[h:gh+h,w:gw+w,2]=cv2.equalizeHist(padded_image[h:gh2+h+1,w:gw2+w+1,2])[gh+1][gw+1]
      
    #convert "histogramized" HSV to bgr
    image=cv2.cvtColor(img,cv2.COLOR_HSV2BGR)

  return image  
