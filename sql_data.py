import mysql.connector

mydb=mysql.connector.connect(
host="localhost",user="root",password="Redhatsql@98",auth_plugin="mysql_native_password")

mycursor=mydb.cursor()
mycursor.execute("CREATE DATABASE My_database03")
mycursor.execute("USE My_database03")
mycursor.execute("CREATE TABLE input(email varchar(255),tv_series varchar(255))")



