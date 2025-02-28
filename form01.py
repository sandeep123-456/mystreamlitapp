import streamlit as st
import sqlite3
from streamlit-option-menu import option_menu

def connect_db():
    conn=sqlite3.connect("mydb.db")
    return conn
def create_Table():
    conn=connect_db()
    cur=conn.cursor()
    cur.execute('CREATE TABLE if not exist student (name text,password text,roll int,branch text)')
    conn.commit()
    conn.close()

def addRecord(data):
    conn=connect_db()
    cur=conn.cursor()
    cur.execute('INSERT INTO STUDENT(name,password,roll,branch)values(?,?,?,?)',data)
    conn.commit()
    conn.close()
def view_record():
    conn=connect_db()
    cur=conn.cursor()
    cur.execute('SELECT * from student')
    return result
def display():
    data=view_record()
    st.write(data)


def signup():
    name=st.text_input("Enter your name")
    password=st.text_input("Enter your password",type="password")
    repass=st.text_input("enter your retype password",type="password")
    roll=st.number_input("enter your roll number",format="%d")
    branch=st.selectbox("enter your branch",options=['cse','aiml','it','iot'])
    if st.button("signin"):
        if password != repass:
            st.error("password not match")
        else:
            addRecord((name,password,roll,branch))


signup()
create_Table()
addRecord()
view_record()
