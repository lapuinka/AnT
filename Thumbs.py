#Fabio Leandro Lapuinka
#Build matrix Imagens Cropped Zoom
import os 
import numpy as np
from PIL import Image
from scipy.ndimage import zoom

senda = 'M:\\sec\\'
saida = 'm:\\img\\imagem_combinada.jpg'

largura, altura, x , y  , c , l , i  , matrix , matriy = 201, 354,  0 , 0 , 0 , 0 , 0 , 1000, 22
imagem_final = Image.new('RGB', (largura * matrix, altura * matriy))
for filename in os.listdir(senda):
     if not filename.endswith(".jpeg") or filename.endswith(".jpg"):
        continue
     if(i >= (matrix * matriy)):
         break
     caminho =  senda + filename 
     img = Image.open(caminho)
     img = img.resize((largura, altura))
     if c % matrix == 0 and c != 0:
         c = 0
         l = l +1
         x = 0
         y = l * altura
     else:
        x = c * largura
        c = c + 1
     i = i + 1
     print(str(i) +":cl[" + str(c-1)+","+str(l)  + "],x:" + str(x) + ",y:" + str(y) +" f: "+ str(filename)) 
     imagem_final.paste(img, (x, y))
imagem_final.show()
imagem_final.save(saida)
