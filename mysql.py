#program to fetch data from mysql database in python
import mysql.connector as sql

mycursor.execute("Select * from student")
for i in mycursor:
     print(i)