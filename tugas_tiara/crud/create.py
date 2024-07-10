import mysql.connector

def create_record(id, nama, jabatan):
    mysb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="kantordesa"
    )

    mycursor = mysb.cursor()

    sql = "INSERT INTO karyawan (id, nama, jabatan) VALUES ( %s, %s, %s)"
    val = (id, nama, jabatan)
    mycursor.execute(sql, val)

    mysb.commit()
    
    print(mycursor.rowcount, "record inserted.")

    mycursor.close()
    mysb.close()