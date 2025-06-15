import mysql.connector as myconn

def connect():
    return myconn.connect(
        host="localhost",
        user="root",
        password="Write Your Own Password Here",
        database="bank_system"
    )