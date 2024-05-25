import os
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from time import strftime
from datetime import datetime
import mysql.connector
import cv2
import numpy as np


class Detect:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1200x600+0+0")
        self.root.title("Detect Face")
        b2 = Button(self.root, text="Detect Face", cursor="hand2", command=self.detect_faces,
                    font=("Helvetica", 16, "bold"), bg="lightblue")
        b2.place(x=300, y=200, width=600, height=200)

  #attendance
    def mark_attendance(self, i, r, n, d):
        file_exists = os.path.isfile("attendance.csv")
        with open("attendance.csv", "a+", newline="\n") as f:

            if not file_exists:
                f.write("ID,Department,Name,Position,Time,Date,Status\n")
            f.seek(0)
            mydatalist = f.readlines()
            name_list = []
            for line in mydatalist:
                entry = line.split(",")
                name_list.append(entry[0])
            if (i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtstring = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtstring},{d1},Present")





  #detect face
    def detect_faces(self):

            def draw_boundary( img, classifier, scaleFactor, minNeighbors, color, text, clf):
                gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

                coord = []
                for (x, y, w, h) in features:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                    id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                    confidence = int((100 * (1 - predict / 300)))
                    conn = mysql.connector.connect(host="localhost", username="root", password="",
                                                   database="face_recognition")
                    my_cursor = conn.cursor()
                    my_cursor.execute("select name from employe where id=" + str(id))
                    n = my_cursor.fetchone()
                    n = "+".join(n)

                    my_cursor.execute("select department from employe where id=" + str(id))
                    d = my_cursor.fetchone()
                    d = "+".join(d)

                    my_cursor.execute("select position from employe where id=" + str(id))
                    p = my_cursor.fetchone()
                    p = "+".join(p)

                    my_cursor.execute("select id from employe where id=" + str(id))
                    i = my_cursor.fetchone()
                    i = "+".join(i)

                    if confidence > 77:
                        cv2.putText(img, f"ID: {i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Department: {d}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Name: {n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Position: {p}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        self.mark_attendance(i, d, n, p)

                    else:
                        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                        cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                    coord = [x, y, w, h]
                return coord

            def recognize( img, clf, faceCascade):

                draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
                return img

            faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.read("classifier.xml")
            video_cap = cv2.VideoCapture(0)
            while True:
                ret, img = video_cap.read()
                if not ret:
                    print("Failed to capture image")
                    break
                img = recognize(img, clf, faceCascade)
                cv2.imshow("Welcome TO face Recognition", img)

                if cv2.waitKey(1) == 13:
                    break
            video_cap.release()
            cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = Detect(root)
    root.mainloop()
