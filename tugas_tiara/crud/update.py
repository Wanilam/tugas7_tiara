
import mysql.connector

def update_record(id,  nama, jabatan ):
    try:
        mysb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="kantordesa"
        )

        mycursor = mysb.cursor()

        sql = "UPDATE karyawan SET id = %s, nama = %s, jabatan = %s WHERE id = %s"
        val = (id, nama, jabatan, id)
        print("Executing SQL:", sql % val)  
        mycursor.execute(sql, val)

        mysb.commit()
        
        print(mycursor.rowcount, "record(s) affected")

    except mysql.connector.Error as err:
        print("Error: {}".format(err))
    finally:
        mycursor.close()
        mysb.close()


