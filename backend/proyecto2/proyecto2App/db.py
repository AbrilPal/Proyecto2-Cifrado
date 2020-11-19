import sqlite3
from sqlite3 import Error
import binascii, os
#from proyecto2App.cifrado import *

db_file = 'files.db'

def conection(db_file):
    cnn = None
    try: 
        #coneccion a la db, la crea si no existe
        cnn = sqlite3.connect(db_file)
        return cnn

    except Error as e:
        print (e)
    return cnn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def find_user (usuario):

    try:
        
        #coneccion a la db, la crea si no existe
        cnn = conection(db_file)
        cur = cnn.cursor()
        cur.execute("SELECT * FROM Usuarios WHERE Usuario=?", (usuario,))
        rows = cur.fetchall()
        print ("Tamaño de respuesta: ", len(rows))
        #hacer login
        
        cnn.commit()
        cnn.close()

        if (len(rows)!=0):
            return 1
        else:
            return 0
    
    except Error as e:
        print (e)
    finally:
        if cnn:
            cnn.close()

def getLogin(usuario, clave):
    print('parametros de getLogin desde db.py------------------------------->')
    print(usuario)
    print(clave)
    # if (find_user(usuario)==1):
    #     try:
            
    #         #coneccion a la db, la crea si no existe
    #         cnn = conection(db_file)
    #         cur = cnn.cursor()
    #         cur.execute("SELECT * FROM Usuarios WHERE Usuario=?", (usuario,))
    #         rows = cur.fetchall()
    #         print ("Tamaño de respuesta: ", len(rows))
    #         for row in rows:
    #             print(row[3]) ##ESTA ES LA CLAVE A COMPARAR

    #         if (clave == row[3]):
    #             print("La clave coincide")
    #         else:
    #             print ("La clave no coincide")
    #         #hacer login
            
    #         cnn.commit()
    #         cnn.close()

    #     except Error as e:
    #         print (e)
    #     finally:
    #         if cnn:
    #             cnn.close()
    # else:
    #     print ("el usuario no existe")


def setRegistro(nombres,apellidos,usuario,clave):
    print('parametros de setRegistro desde db.py------------------------------->')
    print(nombres)
    print(apellidos)
    print(usuario)
    print(clave)
    # if (find_user(usuario)==1):
    #     print ("El usuari ya existe, ingrese otro")
    # else:
              
    #     try: 
    #         #coneccion a la db, la crea si no existe
    #         cnn = conection(db_file)
            
    #         #insert registro
    #         cur = cnn.cursor()
    #         cur.execute('INSERT INTO Usuarios(correo, nombre, usuario, clave) VALUES(?,?,?,?)' ,(correo,nombre,usuario,clave,))
    #         cnn.commit()
    #         cnn.close()

    #     except Error as e:
    #         print (e)
    #     finally:
    #         if cnn:
    #             cnn.close()


def setRegistrarDoc(hashdoc):
    print('parametros de setRegistrarDoc desde db.py------------------------------->')
    print(hashdoc)

    #cuando se registra en la db hay que retornar el codigo de la 
    #db asociado al hash para poder buscarlo despues
    return ('AA01s')

def getValidarDoc(hashdoc, codigo):
    print('parametros de getValidarDoc desde db.py------------------------------->')
    print(hashdoc)
    print(codigo)

    #cuando valida que el hash del codigo ingresado sea el hash de la db entonces
    #se retorna true or false
    return (True)

# conn = conection(db_file)
# sql_create_users_table = """

# CREATE TABLE IF NOT EXISTS Usuarios (
# 	Correo	INTEGER,
# 	Nombre	INTEGER,
# 	Usuario	INTEGER,
# 	Clave	INTEGER
# );"""

# if conn is not None:
#         # create projects table
#         create_table(conn, sql_create_users_table)
        
#         registro("j@gmail.com","jorge","jazmitia","prueba")
# else:
#     print("Error! cannot create the database connection.")

# login("jazmitia","prueba")
