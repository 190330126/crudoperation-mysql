import mysql.connector as a
mydb =a.connect(host="localhost",user="root",passwd="akkiking256",database="studentdb")
mycursor=mydb.cursor()
mycursor.execute("select *from student")
myresult=mycursor.fetchall()
for row in myresult:
    print(row)
    