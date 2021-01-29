import mysql.connector as a
mydb =a.connect(host="localhost",user="root",passwd="akkiking256",database="studentdb")
mycursor=mydb.cursor()
sql ="DELETE FROM student WHERE name='Raju'"
mycursor.execute(sql)
mydb.commit()
