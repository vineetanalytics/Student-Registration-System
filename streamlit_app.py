
import mysql.connector as mysql
import streamlit as st

conn = mysql.connect(host = "localhost", user = "your_username", password = "YOUR_PASSWORD")

cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS SCHOOL_REGISTRACTION_DB")

cursor.execute("USE SCHOOL_REGISTRACTION_DB")

cursor.execute("CREATE TABLE IF NOT EXISTS STUDENT (ID INT PRIMARY KEY AUTO_INCREMENT, ADDMISSION_NO VARCHAR(100), STUDENT_NAME VARCHAR(100), CONTACT_NO varchar(10), CLASS VARCHAR(100), SECTION varchar(100), DISABILITY varchar(100))")

st.title("Student Registraction Form. 👱")

addmission_no = st.text_input(label = "ADDMISSION NO.", placeholder = "Enter your addmission no. : ")
student_name = st.text_input(label = "STUDENT NAME", placeholder = "Enter student name : ")
contact_no = st.text_input(label = "CONTACT NO", placeholder = "Enter contact number : ")
classs = st.text_input(label = "CLASS", placeholder = "Enter your class : ")
section = st.text_input(label = "SECTION", placeholder = "Enter your section : ")
disability = st.selectbox(label = "DISABILITY", options = ["YES","NO"])

if st.button("Submit"):
    cursor.execute("INSERT INTO STUDENT (ADDMISSION_NO, STUDENT_NAME, CONTACT_NO, CLASS, SECTION, DISABILITY) VALUES (%s, %s, %s, %s, %s, %s)",(addmission_no, student_name, contact_no, classs, section, disability))
    conn.commit()
    st.success("Your registration has been successfully submitted", icon = "✅")
