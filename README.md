# facial-recognition
identifying 1000+ students in college is so difficult .so  here comes the solution with facial recognition

pre requirements

python 3.6+ 

python library 
1)numpy 
2)open cv
3)facial_recognition
4)xldr
 
installing library

1)open cmd

2)type "pip install numpy" press enter

3)type "pip install opencv-python" press enter

4)type "pip install xldr"press enter

5)type "pip install face_recognition" press enter

If you are facing error in face_recognition

type "pip install https://pypi.python.org/packages/da/06/bd3e241c4eb0a662914b3b4875fc52dd176a9db0d4a2c915ac2ad8800e9e/dlib-19.7.0-cp36-cp36m-win_amd64.whl#md5=b7330a5b2d46420343fbed5df69e6a3f" press enter

then type "pip install face_recognition"

initially we need to create dataset for identifying name,regno,dob..etc

create a excel file

1	reg	name				dob	dept

2	reg	name				dob	dept

then collect all student photo with regno 

save the excel file as "doball.xlsx"and save all the photos in same location

then run the "creator.py" program which will take some time based on the number of person

after end of program you will get 5 files

"face.npz"

"name.npz"

"reg.npz"

"dob.npz"

"dept.npz"

copy all this file to new folder

run the "recognize.py"

The code is tested for 750+ students we got perfect result

consider subscribing to my youtube channel
https://www.youtube.com/channel/UCFhPVAGq5K12pgHnKZj-EQA





