# MySQL Connector
# Install:
# pip install mysql-connector-python


import mysql.connector as mysql


# Database Connection

conn = mysql.connect(
    host="localhost",
    user="your_username",
    password="YOUR_PASSWORD"
)


cursor = conn.cursor()


# Create Database

cursor.execute(
    "CREATE DATABASE IF NOT EXISTS STUDENT_REGISTRATION_DB"
)


# Select Database

cursor.execute(
    "USE STUDENT_REGISTRATION_DB"
)



# Create Student Table

cursor.execute("""
CREATE TABLE IF NOT EXISTS STUDENT_DETAILS
(
    ID INT AUTO_INCREMENT PRIMARY KEY,
    ADMISSION_NO VARCHAR(50) UNIQUE,
    NAME VARCHAR(100),
    GENDER VARCHAR(20),
    CONTACT VARCHAR(20),
    CLASS VARCHAR(20),
    SECTION VARCHAR(20),
    DISABILITY VARCHAR(10)
)
""")


# Insert Sample Data

cursor.execute("""
INSERT INTO STUDENT_DETAILS
(ADMISSION_NO, NAME, GENDER, CONTACT, CLASS, SECTION, DISABILITY)
VALUES
('STU001','Rahul Sharma','Male','9876543210','10','A','NO'),
('STU002','Priya Singh','Female','9876543211','10','B','NO'),
('STU003','Aman Kumar','Male','9876543212','12','A','YES'),
('STU004','Neha Verma','Female','9876543213','11','C','NO'),
('STU005','Rohit Singh','Male','9876543214','12','B','NO'),
('STU006','Anjali Sharma','Female','9876543215','9','A','NO'),
('STU007','Vikas Kumar','Male','9876543216','10','B','YES'),
('STU008','Sneha Gupta','Female','9876543217','11','A','NO'),
('STU009','Karan Mehta','Male','9876543218','12','C','NO'),
('STU010','Pooja Singh','Female','9876543219','9','B','NO'),
('STU011','Arjun Patel','Male','9876543220','10','C','NO'),
('STU012','Riya Kapoor','Female','9876543221','11','B','NO'),
('STU013','Mohit Sharma','Male','9876543222','12','A','YES'),
('STU014','Kavya Joshi','Female','9876543223','9','C','NO'),
('STU015','Sahil Verma','Male','9876543224','10','A','NO'),
('STU016','Simran Kaur','Female','9876543225','11','C','NO'),
('STU017','Aditya Singh','Male','9876543226','12','B','NO'),
('STU018','Nisha Yadav','Female','9876543227','9','A','NO'),
('STU019','Dev Kumar','Male','9876543228','10','B','YES'),
('STU020','Meera Gupta','Female','9876543229','11','A','NO');
""")


conn.commit()



# Display Data

cursor.execute(
    "SELECT * FROM STUDENT_DETAILS"
)


for data in cursor.fetchall():
    print(data)



# Close Connection

cursor.close()
conn.close()