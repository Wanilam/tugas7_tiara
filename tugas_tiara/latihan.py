import mysql.connector

data = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="matkul",
)

mycursor = data.cursor()
nama = input("masukkan nama: ")
kode = input("masukkan kode: ")
kode = input("masukkan kode: ")
 
sql = "INSERT INTO mata_kuliah (nama,kode) VALUES (%s, %s)"
values = (nama, kode)

mycursor.execute(sql, values)

data.commit()

#myresult = mycursor.fetchall()

mycursor.close()
data.close()


#print(myresult)
