import numpy
import cv2
import math
import warnings
from PIL import Image
import numpy as np

warnings.filterwarnings("ignore")
gorsel1=cv2.imread('gorsel1.png')
gorsel2=cv2.imread('gorsel2.png')
yukseklik=gorsel1.shape[0]
genislik=gorsel1.shape[1]
pixel_sayi=yukseklik*genislik
fark=0

def pixelFark(pixel1,pixel2):
    pixel_fark=0
    for i in range(3):
        pixel_fark=pixel_fark+abs(pixel1[i]-pixel2[i])/255
    return pixel_fark
for i in range(yukseklik):
    for j in range(genislik):
        fark = fark + pixelFark(gorsel1[i][j], gorsel2[i][j])

def farkMatris(matris1,matris2):
    yukselik,genlik=matris1.shape[0], matris1.shape[1]
    matris =np.zeros(shape=(yukseklik,genislik,3), dtype=np.uint8)

    for i in range(yukseklik):
        for j in range(genislik):
            if (pixelFark(matris1[i][j], matris2[i][j])<=0):
                matris[i,j,0]=255
                matris[i,j,0]=255
                matris[i,j,0]=255
                continue
            else:
                matris[i,j,0]=matris2[i,j,0]
                matris[i,j,0]=matris2[i,j,0]
                matris[i,j,0]=matris2[i,j,0] 

                
    img =Image.fromarray(matris,'RGB')
    img.save('farkMatris.png')
    
farklilik_oran=100*fark/(genislik*yukseklik*3)
print("İki gösrsel arası farklilik oranı: "+str(farklilik_oran))
benzerlik_oran=100-farklilik_oran
print("İki görsel arasında ki benzerlik oranı: "+str(benzerlik_oran))
farkMatris(gorsel1, gorsel2)
print("İki görsel arasında ki farklılıklar, fark.png dosyası olarak kaydedildi...")
