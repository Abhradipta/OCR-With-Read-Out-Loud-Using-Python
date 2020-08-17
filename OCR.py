import cv2
import sys
import pytesseract
from gtts import gTTS
import time
import os
from playsound import playsound
import os.path
from os import path
pytesseract.pytesseract.tesseract_cmd=r'Path To The Executable Tesseract File.'
myfile=open("test.txt","w")
myfile.close()
img=input("\nEnter The Path To The Image.\n")
frame = cv2.imread(img)
cv2.imshow('Picture', frame)
sctext=pytesseract.image_to_string(frame)
with open('test.txt', mode='a') as file:
    file.write(sctext)
language='en'
if((os.stat("test.txt").st_size == 0)==False):
    myfile=open("test.txt","r")
    contents=myfile.read()
    myfile.close()
    obj=gTTS(text=contents, lang=language, slow=False)
    obj.save("sample.mp3")
if(path.exists('sample.mp3')==True):
   playsound('sample.mp3')
