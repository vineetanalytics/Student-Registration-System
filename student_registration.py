from tkinter import *
from tkinter import messagebox
import mysql.connector as mysql

conn = mysql.connect(host = "localhost", user = "your_username", password = "YOUR_PASSWORD")

cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS SCHOOL_REGISTRACTION_tk_DB")

cursor.execute("USE SCHOOL_REGISTRATION_tk_DB")

cursor.execute("CREATE TABLE IF NOT EXISTS STUDENT_tk (ID INT PRIMARY KEY AUTO_INCREMENT, STUDENT_NAME VARCHAR(100), FATHER_NAME varchar(100), MOTHER_NAME VARCHAR(100), CONTACT_NUMBER varchar(10), EMAIL_ID varchar(100))")

# ========================= SUBMIT BUTTON FUNCTION =========================
def submit():
    student_name = name_entry.get()
    father_name = fathername_entry.get()
    mother_name = mothername_entry.get()
    contact = contact_number_entry.get()
    email = email_id_entry.get()

    if student_name == "" or father_name == "" or mother_name == "" or contact == "" or email == "":
        messagebox.showerror("Error", "all fields are required ⚠️")
    else:
        textarea.delete("1.0", END)

        textarea.insert(END, "===== STUDENT DETAILS =====\n\n")
        textarea.insert(END, f"Name: {student_name}\n")
        textarea.insert(END, f"Father Name: {father_name}\n")
        textarea.insert(END, f"Mother Name: {mother_name}\n")
        textarea.insert(END, f"Contact Number: {contact}\n")
        textarea.insert(END, f"Email ID: {email}\n")


        cursor.execute(
            """INSERT INTO STUDENT_tk
            (STUDENT_NAME, FATHER_NAME, MOTHER_NAME, CONTACT_NUMBER, EMAIL_ID)
            VALUES (%s, %s, %s, %s, %s)""",
            (student_name, father_name, mother_name, contact, email)
        )

        conn.commit()


        messagebox.showinfo("Successfully", "Data inserted ✅")

# ========================= CLEAR BUTTON FUNCTION =========================
def clear():
    name_entry.delete(0, END)
    fathername_entry.delete(0, END)
    mothername_entry.delete(0, END)
    contact_number_entry.delete(0, END)
    email_id_entry.delete(0, END)

    textarea.delete("1.0", END)

# ========================= EXIT BUTTON FUNTION =========================
def exit_system():
    system.destroy()

# ========================= WINDOW =========================
system = Tk()
system.geometry("1250x700")
system.resizable(False, False)
system.config(background= "#0F172A")
system.title("Student Registration")

# ========================= FIRST FRAME =========================
first_frame = LabelFrame(
    system,
    text="REGISTRATION FORM",
    width= 550,
    height=350,
    background= "#1E293B",
    foreground="#F1F5F9"
)

first_frame.place(x= 15, y = 15, width=550, height=350)
first_frame.pack_propagate(False)


# NAME
name = Label(
    first_frame,
    text= "NAME:",
    background="#1E293B",
    foreground="#F1F5F9", 
    font=("Segoe UI", 10, "bold")
)

name.place(x=20, y=30)
name_entry = Entry(first_frame)
name_entry.place(x=180, y=32)

# FATHER NAME
fathername = Label(
    first_frame, 
    text="FATHER NAME:", 
    background="#1E293B",
    foreground="#F1F5F9", 
    font=("Segoe UI", 10, "bold")
)

fathername.place(x=20, y=60)
fathername_entry = Entry(first_frame)
fathername_entry.place(x=180, y=62)

# MOTHER NAME
mothername = Label(
    first_frame, 
    text="MOTHER NAME:", 
    background="#1E293B",
    foreground="#F1F5F9", 
    font=("Segoe UI", 10, "bold")
)

mothername.place(x=20, y=90)
mothername_entry = Entry(first_frame)
mothername_entry.place(x=180, y=92)

# CONTACT NUMBER
contact_number = Label(
    first_frame, 
    text="CONTACT NUMBER:", 
    background="#1E293B", 
    foreground="#F1F5F9",
    font=("Segoe UI", 10, "bold")
)

contact_number.place(x=20, y=120)
contact_number_entry = Entry(first_frame)
contact_number_entry.place(x=180,y=122)

# EMAIL ID
email_id = Label(
    first_frame, 
    text="EMAIL ID:", 
    background="#1E293B", 
    foreground="#F1F5F9",
    font=("Segoe UI", 10, "bold")
)

email_id.place(x=20, y=150)
email_id_entry = Entry(first_frame)
email_id_entry.place(x=180,y=152)

# ========================= SECOND FRAME =========================
second_frame = LabelFrame(
    system,
    text="STUDENT DETAILS",
    width=650,
    height=350,
    background="#1E293B",
    foreground="#F1F5F9"
)
second_frame.place(x= 585, y=15, width=650, height=350)
second_frame.pack_propagate(False)

textarea = Text(
    second_frame,
    font=("Segoe UI",11),
    background="#FFFFFF",
    foreground="#1E293B",
    borderwidth=1,
    relief="solid"

)
textarea.place(x=10, y= 30, width=620, height=300)

# ========================= ALL BUTTONS =========================
all_button = LabelFrame(
    system,
    text="ALL BUTTON",
    width=1180,
    height=250,
    background="#1E293B",
    foreground="#F1F5F9"
)

all_button.place(x=15, y=385, width=1180, height=250)
all_button.pack_propagate(False)


# SUBMIT
submit_button = Button(
    all_button, 
    text="SUBMIT", 
    background="#2563EB", 
    foreground="#FFFFFF", 
    font=("Segoe UI", 12, "bold"),
    command=submit
)
submit_button.place(x=150, y=100, width=140, height=45)

# CLEAR
clear_button = Button(
    all_button, 
    text="CLEAR", 
    background="#22D3EE", 
    foreground="#0F172A", 
    font=("Segoe UI", 12, "bold"),
    command=clear
)
clear_button.place(x=540, y=100, width=140, height=45)

# EXIT
exit_button = Button(
    all_button, 
    text="EXIT", 
    background="#334155",  
    foreground="#FFFFFF", 
    font=("Segoe UI", 12, "bold"),
    command=exit_system
)
exit_button.place(x=930, y=100, width=140, height=45)


system.mainloop()