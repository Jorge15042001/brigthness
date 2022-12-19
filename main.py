import cv2
import numpy as np

def loadImage (path):
    img = cv2.imread(path)
    shape = np.array(img.shape[:2][::-1])
    shape = (shape/2).astype(int)
    img = cv2.resize(img,shape)
    #  img = img [460:1080,0:560,:]
    return img

def getBScale(name:str):
    if name =="halogena":return 1.6 
    if name =="led":return 1.9 
    if name =="haloled":return 1.5
def getCorrectedImage(name:str):
    blanco =loadImage(f"./input/{name}Fondo.JPG").astype(np.float32)
    blanco *= getBScale(name)

    negro = loadImage(f"./input/fondoNegro.JPG").astype(np.float32)
    data = loadImage(f"./input/{name}Tarjeta.JPG").astype(np.float32)

    correjida = (data - negro)/(blanco - negro)
    #  correjida -= np.min(correjida)
    imMin = np.min(correjida,axis=(0,1))
    imMax = np.max(correjida,axis=(0,1))
    print(imMin)
    print(imMax)
    correjida -= imMin

    
    #  correjida = np.clip(correjida, 0., 1.)

    #  correjida = (correjida-np.min(correjida))/(np.max(correjida)-np.min(correjida))

    return (correjida*255).astype(np.uint8)

#  correccion


#  cv2.imshow("./result/halogena.png",getCorrectedImage("halogena"))
#  cv2.imshow("./result/led.png",getCorrectedImage("led"))
#  cv2.imshow("./result/haloled.png",getCorrectedImage("haloled"))
cv2.imwrite("./result/halogenas/halogena.png",getCorrectedImage("halogena"))
cv2.imwrite("./result/leds/led.png",getCorrectedImage("led"))
cv2.imwrite("./result/haloleds/haloled.png",getCorrectedImage("haloled"))
#  cv2.imwrite("a.png",(correjida*255).astype(np.uint8))

while True:
    try:
        k = cv2.waitKey(5000)
        if chr(k)== "q":break
    except:
        pass
