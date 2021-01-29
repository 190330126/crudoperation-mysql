import mysql.connector as a
mydb =a.connect(host="localhost",user="root",passwd="akkiking256")
mycursor =mydb.cursor()
mycursor.execute("Show Databases")

for db in mycursor:
    print(db)
mycursor.execute("create Database studentdb")
