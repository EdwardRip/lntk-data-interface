"""
Created on Wed Jun 27 18:13:55 2018

@author: hayden.flake
"""

import cv2 as cv
from pyautocad import*
import numpy as np
import array


acad=Autocad(False,True)
ms=acad.model



def has_neighbor(img,i,j,iteration,controlpoints,spaceArray,first):
    img[i,j]=255
    if len(first)==0:
        first=np.array([j,-i,0])
    if iteration==6:
      return np.append(first,np.append(np.array([j,-i,0]),has_neighbor(img,i,j,iteration+1,controlpoints+1,spaceArray,np.array([0,0,0]))))  
    elif iteration%6==0:
        print("adding")
        print( has_neighbor(img,i,j,iteration+1))
        return np.append(np.array([j,-i,0]),has_neighbor(img,i,j,iteration+1,controlpoints+1,spaceArray,np.array([0,0,0])))
    if i==img.shape[0]-1 or j==img.shape[1]-1 or controlpoints==50:
        return np.array([])
    if img[i+1,j-1]==0 and 1 in spaceArray:
        return has_neighbor(img,i+1,j-1,iteration+1,controlpoints,[1,2,3,4,6,7,8],first)
    if img[i+1,j]==0 and 2 in spaceArray:
       return has_neighbor(img,i+1,j,iteration+1,controlpoints,[1,2,3,4,5,7,8],first)
    if img[i+1,j+1]==0 and 3 in spaceArray:
       return has_neighbor(img,i+1,j+1,iteration+1,controlpoints,[1,2,3,4,5,6,8],first)
    if img[i,j+1]==0 and 4 in spaceArray:
        return has_neighbor(img,i,j+1,iteration+1,controlpoints,[1,2,3,4,5,6,7],first)
    
    
    if img[i-1,j+1]==0 and 5 in spaceArray:
        return has_neighbor(img,i-1,j+1,iteration+1,controlpoints,[2,3,4,5,6,7,8],first)
    if img[i-1,j]==0 and 6 in spaceArray:
        return has_neighbor(img,i-1,j,iteration+1,controlpoints,[1,3,4,5,6,7,8],first)
    if img[i-1,j-1]==0 and 7 in spaceArray:
        return has_neighbor(img,i-1,j-1,iteration+1,controlpoints,[1,2,4,5,6,7,8],first)
    if img[i,j-1]==0 and 8 in spaceArray:
        return has_neighbor(img,i,j-1,iteration+1,controlpoints,[1,2,3,5,6,7,8],first)
    return np.array([])

imgO = cv.imread('wallup.jpg')



img=cv.cvtColor(imgO,cv.COLOR_BGR2GRAY)
ret,img=cv.threshold(img,90,255,cv.THRESH_BINARY)
img=cv.Canny(img,100,200)
img=255-img
cv.imshow("image",img)
cv.waitKey(0)
for i in range(0,img.shape[0]):
    for j in range(0,img.shape[1]):
        if img[i,j]==0:
            plotpoints=has_neighbor(img,i,j,1,0,[1,2,3,4,5,6,7,8],np.array([]))
            print(plotpoints)
            print(len(plotpoints))
            if len(plotpoints)>4:
                print("got one")
                obj=ms.addSpline(aDouble(plotpoints.flatten()),APoint(0.0,0.0,0),APoint(0.0,0.0,0))
                colAr=imgO[i,j]
                col=obj.TrueColor
                col.setRGB(int(colAr[2]),int(colAr[1]),int(colAr[0]))
                obj.TrueColor=col

cv.imshow("img",img)
cv.waitKey(0)

cv.destroyAllWindows() 