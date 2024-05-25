import os
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import numpy as np

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1200x600+0+0")
        self.root.title("Train Data")

        b4 = Button(self.root,text="Train Data", cursor="hand2", command=self.train_classifier, font=("Helvetica", 16, "bold"), bg="lightblue")
        b4.place(x=300, y=200, width=600, height=200)

    def train_classifier(self):
        data_dir = "data"
        if not os.path.exists(data_dir):
            messagebox.showerror("Error", "Data directory does not exist")
            return

        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]
        if not path:
            messagebox.showerror("Error", "No images found in data directory")
            return

        faces = []
        ids = []

        for image in path:
            print(f"Processing image: {image}")
            img = Image.open(image).convert('L')
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1)

        if len(faces) == 0 or len(ids) == 0:
            messagebox.showerror("Error", "No valid images found for training")
            return

        ids = np.array(ids)

        # Train classifier and save
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training datasets completed")

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
