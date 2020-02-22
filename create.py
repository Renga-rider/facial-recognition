import cv2
import numpy as np
import os
import face_recognition
import xlrd
from numpy import savetxt
from numpy import loadtxt
wb = xlrd.open_workbook("doball.xlsx") #open the excel sheet contain name,reg,dob,dept
sheet = wb.sheet_by_index(0) 
sheet.cell_value(0, 0) 
known_face_encodings = []#variable for storing facedata
reg=[]#variable for storing reg
dept=[]#variable for storing dept
dob=[]#variable for storing dob
names=[]#variable for storing names
for img_name in os.listdir():
    if img_name.endswith(".jpg"):#reading the jpg image from folder
        
        cmp=int(img_name.split('.')[0])#removing the extension from name and converting name to int
        name=str(img_name)
        print(name)
        image = face_recognition.load_image_file(name)#loading the image
        image_face_encoding = face_recognition.face_encodings(image)[0]#encoding image to data
        
        for z in range(sheet.nrows):
                    s=sheet.cell_value(z, 1)
                    s=int(s)
                    s=abs(s)
                    if(s==cmp):#comparing the image regno with excel sheet
                        print(int(sheet.cell_value(z, 1)))
                        dob1=int(sheet.cell_value(z, 6))#getting respective dob
                        print(dob1)
                        dob.append(dob1)#storing in dob variable
                        name1=sheet.cell_value(z, 2)#getting respective name
                        print(name1)
                        name1=str(name1)
                        names.append(name1)#storing in name variable
                        dept1=sheet.cell_value(z, 7)#getting respective dept
                        dept.append(dept1)#storing in dept variable
                        print(dept1)
                        reg.append(int(img_name.split('.')[0]))#storing
                        known_face_encodings.append(image_face_encoding)#storing in a array
                           
        
savetxt('face.npz',known_face_encodings , delimiter=',')#saving the face data    
savetxt('reg.npz',reg, delimiter=',')#saving the reg
savetxt('name.npz',names,fmt='%s', delimiter=',')#saving the name as string
savetxt('dob.npz',dob, delimiter=',')#saving the dob
savetxt('dept.npz',dept,fmt='%s', delimiter=',')#saving the dept as string
print("end")#end of program
        
