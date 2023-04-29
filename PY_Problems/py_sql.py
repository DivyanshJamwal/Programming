import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root"
)
mycursor = mydb.cursor()
mycursor.execute("Create Database LPU")
print("Database Created")