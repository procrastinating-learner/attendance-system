from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Employe:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1200x600+0+0")
        self.root.title("Employe")
        # Variables
        self.var_id = StringVar()
        self.var_dep = StringVar()
        self.var_name = StringVar()
        self.var_adress = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_pos = StringVar()
        self.var_radio1 = StringVar()
        self.var_radio2 = StringVar()

        self.var_search_criteria = StringVar()
        self.var_search_text = StringVar()

        # bg image
        img = Image.open(r"C:\Users\pc\PycharmProjects\face recognition\images\employe.png")
        img = img.resize((1200, 600), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0, width=1200, height=600)

        # main frame
        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=20, y=50, width=1160, height=520)

        # left frame
        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Employe Details",
                                font=("Helvetica", 14, "bold"))
        left_frame.place(x=10, y=10, width=550, height=500)

        # Employe ID
        EmployeId_label = Label(left_frame, text="EmployeId:", font=("Helvetica", 10, "bold"), bg="white")
        EmployeId_label.grid(row=0, column=0, padx=10, sticky=W)
        EmployeId_entry = ttk.Entry(left_frame, width=20, textvariable=self.var_id, font=("Helvetica", 11, "bold"))
        EmployeId_entry.grid(row=0, column=1, padx=10, sticky=W)

        # Employe Name
        EmployeName_label = Label(left_frame, text="Employe Name:", font=("Helvetica", 10, "bold"), bg="white")
        EmployeName_label.grid(row=1, column=0, padx=10, sticky=W)
        EmployeName_entry = ttk.Entry(left_frame, textvariable=self.var_name, width=20, font=("Helvetica", 11, "bold"))
        EmployeName_entry.grid(row=1, column=1, padx=10, sticky=W)

        # Employe Email
        EmployeEmail_label = Label(left_frame, text="Email:", font=("Helvetica", 10, "bold"), bg="white")
        EmployeEmail_label.grid(row=3, column=0, padx=10, sticky=W)
        EmployeEmail_entry = ttk.Entry(left_frame, width=20, textvariable=self.var_email, font=("Helvetica", 11, "bold"))
        EmployeEmail_entry.grid(row=3, column=1, padx=10, sticky=W)

        # Employe Address
        EmployeAddress_label = Label(left_frame, text="Address:", font=("Helvetica", 10, "bold"), bg="white")
        EmployeAddress_label.grid(row=4, column=0, padx=10, sticky=W)
        EmployeAddress_entry = ttk.Entry(left_frame, width=20, textvariable=self.var_adress, font=("Helvetica", 11, "bold"))
        EmployeAddress_entry.grid(row=4, column=1, padx=10, sticky=W)

        # Phone
        Phone_label = Label(left_frame, text="Phone Number:", font=("Helvetica", 10, "bold"), bg="white")
        Phone_label.grid(row=5, column=0, padx=10, sticky=W)
        Phone_entry = ttk.Entry(left_frame, width=20, textvariable=self.var_phone, font=("Helvetica", 11, "bold"))
        Phone_entry.grid(row=5, column=1, padx=10, sticky=W)

        # Department
        Dep_label = Label(left_frame, text="Department:", font=("Helvetica", 10, "bold"), bg="white")
        Dep_label.grid(row=6, column=0, padx=10, sticky=W)
        Dep_combo = ttk.Combobox(left_frame, textvariable=self.var_dep, font=("Helvetica", 10, "bold"), width=20, state="readonly")
        Dep_combo["values"] = ("Select Department", "Management", "Human Resources", "Finance", "Maintenance", "IT", "etc.")
        Dep_combo.current(0)
        Dep_combo.grid(row=6, column=1, padx=10, sticky=W)

        # Employe Position
        position_label = Label(left_frame, text="Position:", font=("Helvetica", 10, "bold"), bg="white")
        position_label.grid(row=7, column=0, padx=10, sticky=W)
        position_entry = ttk.Entry(left_frame, width=20, textvariable=self.var_pos, font=("Helvetica", 11, "bold"))
        position_entry.grid(row=7, column=1, padx=10, sticky=W)

        # Work hours
        Hours_label = Label(left_frame, text="Work Hours:", font=("Helvetica", 10, "bold"), bg="white")
        Hours_label.grid(row=8, column=0, padx=10, sticky=W)
        Start_label = Label(left_frame, text="From:", font=("Helvetica", 10, "bold"), bg="white")
        Start_label.grid(row=9, column=0, padx=10, sticky=W)
        start_entry = ttk.Entry(left_frame, width=15, font=("Helvetica", 11, "bold"))
        start_entry.grid(row=9, column=1, padx=10, sticky=W)
        End_label = Label(left_frame, text="To:", font=("Helvetica", 10, "bold"), bg="white")
        End_label.grid(row=9, column=2, padx=10, sticky=W)
        End_entry = ttk.Entry(left_frame, width=15, font=("Helvetica", 11, "bold"))
        End_entry.grid(row=9, column=3, padx=5, sticky=W)

        # Employe pic
        Photo_label = Label(left_frame, text="Employe Picture Available:", font=("Helvetica", 10, "bold"), bg="white")
        Photo_label.grid(row=10, column=0, padx=10, sticky=W)
        radiobut1 = ttk.Radiobutton(left_frame, text="Yes", variable=self.var_radio1, value="Yes")
        radiobut1.grid(row=11, column=0)
        radiobut2 = ttk.Radiobutton(left_frame, text="No", variable=self.var_radio2, value="No")
        radiobut2.grid(row=11, column=1)

        # Buttons
        btn_frame = Frame(left_frame, bd=None, relief=RIDGE, bg="white")
        btn_frame.place(x=5, y=300, width=520, height=130)

        save_btn = Button(btn_frame, text="Save", width=20, command=self.add_data, font=("Helvetica", 10, "bold"), bg="grey", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Update", command=self.update_data, width=20, font=("Helvetica", 10, "bold"), bg="grey", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Delete", command=self.delete_data, width=20, font=("Helvetica", 10, "bold"), bg="grey", fg="white")
        delete_btn.grid(row=1, column=0)

        take_btn = Button(btn_frame, text="Take Photo", command=self.generate_data, width=20, font=("Helvetica", 10, "bold"), bg="grey", fg="white")
        take_btn.grid(row=0, column=2)

        # right frame
        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Employe Details",
                                 font=("Helvetica", 14, "bold"))
        right_frame.place(x=570, y=10, width=550, height=500)

        # search system
        searchframe = LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE, text="Search Employes",
                                font=("Helvetica", 10, "bold"))
        searchframe.place(x=5, y=20, width=540, height=120)
        Search_label = Label(searchframe, text="Search By:", font=("Helvetica", 10), bg="white")
        Search_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)
        Search_combo = ttk.Combobox(searchframe, textvariable=self.var_search_criteria, font=("Helvetica", 10, "bold"), width=20, state="readonly")
        Search_combo["values"] = ("Select Criteria", "Id", "Position", "Department", "Performance", "Phone No")
        Search_combo.current(0)
        Search_combo.grid(row=0, column=1, padx=10, sticky=W)
        Search_entry = ttk.Entry(searchframe, textvariable=self.var_search_text, width=20, font=("Helvetica", 11, "bold"))
        Search_entry.grid(row=0, column=2, padx=10, sticky=W)

        search_btn = Button(searchframe, text="Search", command=self.search_data, width=10, font=("Helvetica", 10, "bold"), bg="grey", fg="white")
        search_btn.grid(row=1, column=1)

        showall_btn = Button(searchframe, text="Show All", command=self.fetch_data, width=10, font=("Helvetica", 10, "bold"), bg="grey", fg="white")
        showall_btn.place(x=226, y=42)

        # results frame
        resultframe = Frame(right_frame, bd=2, bg="white", relief=RIDGE)
        resultframe.place(x=5, y=140, width=540, height=320)

        scroll_x = ttk.Scrollbar(resultframe, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(resultframe, orient=VERTICAL)
        self.Employe_table = ttk.Treeview(resultframe, column=("ID", "Name", "Address", "Email", "Phone", "Department", "Position", "Photo"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Employe_table.xview)
        scroll_y.config(command=self.Employe_table.yview)
        self.Employe_table.heading("ID", text="EmployeId")
        self.Employe_table.heading("Name", text="EmployeName")
        self.Employe_table.heading("Address", text="Address")
        self.Employe_table.heading("Email", text="Email")
        self.Employe_table.heading("Phone", text="Phone")
        self.Employe_table.heading("Department", text="Department")
        self.Employe_table.heading("Position", text="Position")
        self.Employe_table.heading("Photo", text="Photo")
        self.Employe_table["show"] = "headings"
        self.Employe_table.pack(fill=BOTH, expand=1)
        self.fetch_data()

    # Functions
    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_id.get() == "" or self.var_name.get() == "" or self.var_pos.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="", database="face_recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into Employe values(%s,%s,%s,%s,%s,%s,%s,%s)",
                                  (
                                      self.var_id.get(),
                                      self.var_name.get(),
                                      self.var_phone.get(),
                                      self.var_adress.get(),
                                      self.var_email.get(),
                                      self.var_dep.get(),
                                      self.var_pos.get(),
                                      self.var_radio1.get()
                                  ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Employe Details Added", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    # Fetch data from database
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="", database="face_recognition")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from Employe")
        data = my_cursor.fetchall()
        if len(data) != 0:
            self.Employe_table.delete(*self.Employe_table.get_children())
            for i in data:
                self.Employe_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # Update data in database
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_id.get() == "" or self.var_name.get() == "" or self.var_pos.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want to modify this info?", parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="", database="face_recognition")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update Employe set name=%s, phone=%s, address=%s, email=%s, department=%s, position=%s, photo=%s where id=%s", (
                        self.var_name.get(),
                        self.var_phone.get(),
                        self.var_adress.get(),
                        self.var_email.get(),
                        self.var_dep.get(),
                        self.var_pos.get(),
                        self.var_radio1.get(),
                        self.var_id.get()
                    ))
                else:
                    if not Update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Employe Details Updated Successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    # Delete data from database
    def delete_data(self):
        if self.var_id.get() == "":
            messagebox.showerror("Error", "Employe ID required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Employe Delete", "Do you want to delete this employe?", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="", database="face_recognition")
                    my_cursor = conn.cursor()
                    sql = "delete from Employe where id=%s"
                    val = (self.var_id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Employe Deleted Successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    # Take photo
    def generate_data(self):
        if self.var_dep.get() == "Select Department" or self.var_id.get() == "" or self.var_name.get() == "" or self.var_pos.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="",
                                               database="face_recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from employe")
                myresult=my_cursor.fetchall()
                id=0
                for i in myresult:
                    id+=1
                my_cursor.execute(
                    "update Employe set name=%s, phone=%s, address=%s, email=%s, department=%s, position=%s, photo=%s where id=%s",
                    (
                        self.var_name.get(),
                        self.var_phone.get(),
                        self.var_adress.get(),
                        self.var_email.get(),
                        self.var_dep.get(),
                        self.var_pos.get(),
                        self.var_radio1.get(),
                        self.var_id.get()==id+1
                    ))

                conn.commit()
                self.fetch_data()
                conn.close()
                # Load data on face frontals
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y + h, x:x + w]
                        return face_cropped

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if not ret:
                        break
                    cropped_face = face_cropped(my_frame)
                    if cropped_face is not None:
                        img_id += 1
                        face = cv2.resize(cropped_face, (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = f"data/user.{id}.{img_id}.jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or img_id == 100:
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Dataset Generated")
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    # Search data from database
    def search_data(self):
        search_by = self.var_search_criteria.get()
        search_text = self.var_search_text.get()
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="", database="face_recognition")
            my_cursor = conn.cursor()
            if search_by == "Id":
                query = "select * from Employe where id LIKE '%" + search_text + "%'"
            elif search_by == "Position":
                query = "select * from Employe where position LIKE '%" + search_text + "%'"
            elif search_by == "Department":
                query = "select * from Employe where department LIKE '%" + search_text + "%'"
            elif search_by == "Phone No":
                query = "select * from Employe where phone LIKE '%" + search_text + "%'"
            else:
                query = "select * from Employe"

            my_cursor.execute(query)
            data = my_cursor.fetchall()
            if len(data) != 0:
                self.Employe_table.delete(*self.Employe_table.get_children())
                for i in data:
                    self.Employe_table.insert("", END, values=i)
                conn.commit()
            conn.close()
        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Employe(root)
    root.mainloop()
