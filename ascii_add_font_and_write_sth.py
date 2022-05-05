import cv2
import numpy as np


"""
OpenCV kütüphanesinde bir fontun üzerine yazı yazmak için 
cv2.putText() fonksiyonu kullanılır. 

cv2putText(imaj,text,sol_alt_köşe,sağ_alt_köşe,font,ölçek,renk,çizgi_tipi)


HERSHEY fontları türkçe karakter desteklemez.

"""

fontlar = ["FONT_HERSHEY_SIMPLEX","FONT_HERSHEY_PLAIN","FONT_HERSHEY_DUPLEX", "FONT_HERSHEY_COMPLEX", "FONT_HERSHEY_TRIPLEX", "FONT_HERSHEY_COMPLEX_SMALL", "FONT_HERSHEY_SCRIPT_SIMPLEX", "FONT_HERSHEY_SCRIPT_COMPLEX"]

imaj = np.ones((720,780,3),np.uint8)*255  # beyaz imaj

for j in range(8):
    cv2.putText(imaj, fontlar[j], (20,40+j*40), j, 1.1, (0,0,0,), 1)
    
italik = 16

for j in range(8):
    cv2.putText(imaj, fontlar[j] + '(italik)', (20,400+j*40), j+italik, 1.1, (0,0,0,), 1)
    
cv2.imshow("imaj" , imaj)

while True:
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27 or k == ord("q"):
        break
cv2.destroyAllWindows()
    

