import mysql.connector as a
mydb =a.connect(host="localhost",user="root",passwd="akkiking256",database="studentdb")
mycursor=mydb.cursor()
form="Insert into student(name,rno) values(%s,%s)"
students=[("Ravi",202),("Raju",187),("vigneshwar",80)]
mycursor.executemany(form,students)
mydb.commit()