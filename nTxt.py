import mysql.connector as cnx
# import getpass

# password = getpass()

try:
    mydb = cnx.connect(
        host = "localhost",
        user = "root",
        password = "@dztmHc3e"
    )




except:
    print("Wrong Unername or Password. Try again.")

else:
    print("Coonected")



cursor = cnx.cursor()

cursor.execute("SHOW DATABASES")

for x in cursor:
    print(x)
