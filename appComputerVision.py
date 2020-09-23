
#  Developed By @boscobecker 
#  Aplicação de  Visão computacional, usando sorriso e olhos e rosto real-time usando OPENCV e Python. 
#  A ideia é reconhecer rostos, um soriso ou os olhos usando a webcam do seu notebook.
#  O intuito da apicação é entender como funciona o OPENCV e Visão computacional(Computer Vision) usando Python.
#  Curitiba -  Paraná  - Brasil

import cv2
import time
from PIL import ImageFont, ImageDraw, Image

# Call the haarcascade to use in 
arqCasc1 = 'haarcascade/haarcascade_frontalface_default.xml'
arqCasc2 = 'haarcascade/haarcascade_eye.xml'
arqCasc3 = 'haarcascade/haarcascade_smile.xml' 

faceCascade1 = cv2.CascadeClassifier(arqCasc1) #Face
faceCascade2 = cv2.CascadeClassifier(arqCasc2) #Eyes
faceCascade3 = cv2.CascadeClassifier(arqCasc3) #Smile

#CaptureDevice = camera, make the call
webcam = cv2.VideoCapture(0, cv2.CAP_DSHOW) 

#Counters
faceCounter = 0 
olhoCounter = 0
smileCounter = 0

while True:

    #Use the webcam Image
    ret, imagem = webcam.read() 
    
    #Mirror the image
    imagem = cv2.flip(imagem,180) 
    
    faces = faceCascade1.detectMultiScale(
        imagem,
        minNeighbors=20,
        minSize=(30, 30),
	maxSize=(300,300)
    )

    olhos = faceCascade2.detectMultiScale(
        imagem,
        minNeighbors=20,
        minSize=(10, 10),
	maxSize=(90,90)
    )
 
    smile = faceCascade3.detectMultiScale(
        imagem, 
        scaleFactor = 1.8, 
    minNeighbors = 20
    )   
  
    # describe the type of font   
    font = cv2.FONT_HERSHEY_SIMPLEX 
  
    # inserting text on video 
    cv2.putText(imagem,'Para finalizar pressione a tecla (Q).',(10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))  
    
    #Smile counter
    cv2.putText(imagem,'Rosto(s): '+ str(faceCounter), (5,400), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 245))    

    #Olho counter
    cv2.putText(imagem,'Olho(s): '+ str(olhoCounter), (5,430), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0))    

    #Sorriso counter
    cv2.putText(imagem,'Sorriso(s): '+ str(smileCounter), (5 460), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0))   

    # Draw the hour in screen real-time
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t) 
    cv2.putText(imagem, str(current_time), (520,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0)) 

    # Draw the rectangle on face, eyes and smile detected
    for (x, y, w, h) in faces:
        cv2.rectangle(imagem, (x, y), (x+w, y+h), (0, 0, 245), 4)
        cv2.putText(imagem,'Rosto detectado', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0, 0, 245)) 
        faceCounter=faceCounter+1
       # print("Rosto detectados: " + str(faceCounter))
    
    for (x, y, w, h) in olhos:
        cv2.rectangle(imagem, (x, y), (x+w, y+h), (255, 255, 0), 2)        
        cv2.putText(imagem,'Olhos', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0)) 
        olhoCounter=olhoCounter+1
       # print("Olhos detectados: " + str(olhoCounter))

    for (x, y, w, h) in smile:
       cv2.rectangle(imagem, (x, y), (x+w, y+h), (255, 0, 0), 5)        
       cv2.putText(imagem,'Sorriso', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0)) 
       smileCounter=smileCounter+1
      # print("Sorrisos detectados: " + str(smileCounter))
    
    #Show the imagem using your webcam
    cv2.imshow('Webcam On', imagem)

    #Exit of program press "Q" key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

 #release the webcam use
webcam.release()

#Close all windows open
cv2.destroyAllWindows() 