import os
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from employe import Employe
from train import Train
from detect_face import Detect

class face_recognition_system:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1200x600+0+0")
        self.root.title("face recognition system")
        #bg image
        img = Image.open(r"C:\Users\pc\PycharmProjects\face recognition\images\employe.png")
        img = img.resize((1200, 600), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1200,height=600)
        #employe button
        b1=Button(bg_img,text="Employe details",command=self.employe_details,cursor="hand2",font=("Helvetica", 16, "bold"),bg="lightblue")
        b1.place(x=200,y=100,width=200,height=200)
        # Detect face button
        b2 = Button(bg_img, text="Detect Face",command=self.face_datas, cursor="hand2", font=("Helvetica", 16, "bold"), bg="lightblue")
        b2.place(x=480, y=100, width=200, height=200)
        # attendance face button
        b3 = Button(bg_img, text="Attendance ", cursor="hand2", font=("Helvetica", 16, "bold"), bg="lightblue")
        b3.place(x=760, y=100, width=200, height=200)
        # Train button
        b4 = Button(bg_img, text="Train Data",command=self.train_datas, cursor="hand2", font=("Helvetica", 16, "bold"), bg="lightblue")
        b4.place(x=200, y=350, width=200, height=200)
        # photos button
        b5 = Button(bg_img, text="Photos",command=self.open_img, cursor="hand2", font=("Helvetica", 16, "bold"), bg="lightblue")
        b5.place(x=480, y=350, width=200, height=200)

#functions
    def employe_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Employe(self.new_window)
    def open_img(self):
        os.startfile("data")

    def train_datas(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
    def face_datas(self):
        self.new_window=Toplevel(self.root)
        self.app=Detect(self.new_window)





if __name__ == "__main__":
    root = Tk()
    obj = face_recognition_system(root)
    root.mainloop()
