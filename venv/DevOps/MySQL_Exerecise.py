import pymysql as pymysql

conn = pymysql.connect(host='remotemysql.com', port=3306, user='r6bRKeitLD', passwd='FurxmtHKRh', db='r6bRKeitLD')

cursor = conn.cursor()


cursor.execute("INSERT into `r6bRKeitLD`.`Dogs`(`name`, `age`, `breed`) VALUES ('Joe', 3, 'Pug');")
cursor.execute("INSERT INTO `r6bRKeitLD`.`Dogs` (`name`, `age`, `breed`) VALUES ('Yoko', 6, 'Shikuku')")
cursor.execute("INSERT INTO `r6bRKeitLD`.`Dogs` (`name`, `age`, `breed`) VALUES ('Sam', 5, 'Canaan Dog')")
cursor.execute("UPDATE `r6bRKeitLD`.`Dogs` SET age = '7' WHERE name = 'Yoko'")
cursor.execute("DELETE FROM `r6bRKeitLD`.`Dogs` WHERE name = 'Sam' ")
conn.commit()

cursor.execute("SELECT * FROM r6bRKeitLD.Dogs;")

for row in cursor:
    print(row)


cursor.close()
conn.close()