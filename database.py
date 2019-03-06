#program to fetch data from mtsql database in python
import mysql.connector as sql
mydb =  sql.connect(host="localhost",user="username",passwd="*****",database="*****")

mycursor = mydb.cursor()
mycursor.execute("Select * from student")         #enetr the aommand you want to fetch data of
result = mycursor.fetchall()            #fetch all data from database
#result = mycursor.fetchone()             #fetch first column from database
for i in result:
     print(i)            #print result of each row in different line
#print (result)          print result in one line