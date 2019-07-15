# Establishing a connection to DB
import pymysql as pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='Madrid16', db='Users')

# Getting a cursor from Database
cursor = conn.cursor()

# Getting all data from table “users”
cursor.execute("SELECT * FROM r6bRKeitLD.Dogs;")

# Iterating table and printing all users
for row in cursor:
    print(row)

#cursor.execute("Delete FROM Users.Players WHERE name = 'WW'")
#cursor.execute("INSERT INTO Users.Players(ID,Name)VALUES(4,'WW');")
cursor.execute("UPDATE Users.Players SET id = '2' WHERE name = 'Adiel';")

conn.commit()


cursor.close()
conn.close()
