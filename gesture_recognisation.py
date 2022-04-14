from cProfile import label
from tkinter import*
import numpy as np
import cv2
from tkinter import ttk
from turtle import title
from PIL import Image,ImageTk 


class face_rg1: 
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognisation system")

        #Image 1
        img = Image.open(r"D:/IT Document/Sem-4/SGP/Mouse/Project_Images/Vartual_mouse_system.webp")
        img=img.resize((500,200),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        flbl=Label(self.root,image=self.photoimg)
        flbl.place(x=0,y=0,width=500,height=180)

        #Image 2
        title_lbl = Label(self.root,text="Vertual mouse System",font=("Playfair Display",20,"bold"),bg="red",fg="cyan")
        title_lbl.place(x=500,y=0,width=500,height=180)


        #Image 3
        img3 = Image.open(r"D:\IT Document\Sem-4\SGP\Mouse\Project_Images\mouse.png")
        img3=img3.resize((500,200),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        flbl=Label(self.root,image=self.photoimg3)
        flbl.place(x=1000,y=0,width=500,height=180)

        img4 = Image.open(r"D:\IT Document\Sem-4\SGP\Mouse\Project_Images\facial-recognition.jpg")
        img4=img4.resize((1530,680),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=180,width=1530,height=680)

    

         # left label frame

        left_frame = LabelFrame(bd=2,relief = RIDGE,font=("times new roman",12,"bold"))
        left_frame.place(x=400,y=250,width=200,height=400)

      

        flbl=Label(left_frame,bg="red")
        flbl.place(x=0,y=0,width=700,height=250)

     



        Current_course = LabelFrame(left_frame,bd=2,relief = RIDGE,font=("times new roman",12,"bold"),bg="orange")
        Current_course.place(x=0,y=253,width=200,height=150)

        dep_label = Button(Current_course,text="Using hand\nRecognisation", command = open_camera,font=("times new roman",20,"bold"))
        dep_label.grid(row=2,column=0,pady=5,sticky=W)

        #Right frame
        right_frame = LabelFrame(bd=2,relief = RIDGE,font=("times new roman",12,"bold"))
        right_frame.place(x=800,y=250,width=200,height=400)

        

        flbl=Label(right_frame,bg="red")
        flbl.place(x=0,y=0,width=700,height=250)

        Current_course = LabelFrame(right_frame,bd=2,relief = RIDGE,font=("times new roman",12,"bold"),bg="orange")
        Current_course.place(x=0,y=253,width=200,height=150)

        dep_label = Button(Current_course,text="Using Facial\nMovements", command = open_camera,font=("times new roman",20,"bold"))
        dep_label.grid(row=2,column=0,pady=5,sticky=W)


        #center frame
        center_frame = LabelFrame(bd=2,relief = RIDGE,font=("times new roman",12,"bold"),bg="red")
        center_frame.place(x=400,y=670,width=600,height=38)

     
        save_btn = Label(center_frame,text="Choose one of them",width=66,font=("times new roman",12,"bold"),bg="Red",fg="black")
        save_btn.grid(row=0,column=0)

class face_rg:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognisation system")

        #Image 1
        img = Image.open(r"D:/IT Document/Sem-4/SGP/Mouse/Project_Images/Vartual_mouse_system.webp")
        img=img.resize((500,200),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        flbl=Label(self.root,image=self.photoimg)
        flbl.place(x=0,y=0,width=500,height=180)

        #Image 2
        title_lbl = Label(self.root,text="Vertual mouse System",font=("Playfair Display",20,"bold"),bg="red",fg="cyan")
        title_lbl.place(x=500,y=0,width=500,height=180)

        

        #Image 3
        img3 = Image.open(r"D:\IT Document\Sem-4\SGP\Mouse\Project_Images\mouse.png")
        img3=img3.resize((500,200),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        flbl=Label(self.root,image=self.photoimg3)
        flbl.place(x=1000,y=0,width=500,height=180)

        img4 = Image.open(r"D:\IT Document\Sem-4\SGP\Mouse\Project_Images\facial-recognition.jpg")
        img4=img4.resize((1530,680),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=180,width=1530,height=680)



        main_frame = Frame(bd= 2)
        main_frame.place(x=370,y=200,width=730,height=565)

        #left frame
        frame = LabelFrame(main_frame,bd=2,relief = RIDGE,text="Mouse Buttons",font=("times new roman",12,"bold"))
        frame.place(x=10,y=10,width=710,height=535)

        btn_frame=Frame(frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=150,width=200,height=200)
        
        save_btn = Button(btn_frame,text="Start",command = open_popup,width=21,font=("times new roman",12,"bold"),bg="orange",fg="black")
        save_btn.grid(row=3,column=0,pady=15)

        save_btn = Button(btn_frame,text="How to?",width=21,font=("times new roman",12,"bold"),bg="orange",fg="black")
        save_btn.grid(row=5,column=0,pady=15)

        save_btn = Button(btn_frame,text="Exit",width=21,font=("times new roman",12,"bold"),bg="orange",fg="black")
        save_btn.grid(row=7,column=0,pady=15)

         #Right frame

        btn_frame=Frame(frame,bd=2,relief=RIDGE)
        btn_frame.place(x=507,y=150,width=200,height=200)
       

        save_btn = Button(btn_frame,text="About us",width=21,font=("times new roman",12,"bold"),bg="orange",fg="black")
        save_btn.grid(row=7,column=0,pady=150)

def open_camera():
    faceCascade = cv2.CascadeClassifier('D:\IT Document\Sem-4\SGP\Mouse\haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)
    cap.set(3,640)
    cap.set(4,480)
    while True:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,     
            scaleFactor=1.2,
            minNeighbors=5,     
            minSize=(20, 20)
        )
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]  
        cv2.imshow('video',img)
        k = cv2.waitKey(30) & 0xff
        if k == 27: 
            break
    cap.release()
    cv2.destroyAllWindows()
def open_popup():
   obj = face_rg1(root)
   root.mainloop()
if __name__ == "__main__":
        root=Tk()
        obj = face_rg(root)
        root.mainloop()