import sqlite3
from sqlite3 import Error
import binascii, os
from cifrado import *

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

def registro(correo,nombre,usuario,clave):
    if (find_user(usuario)==1):
        print ("El usuari ya existe, ingrese otro")
    else:
              
        try: 
            #coneccion a la db, la crea si no existe
            cnn = conection(db_file)
            
            #insert registro
            cur = cnn.cursor()
            cur.execute('INSERT INTO Usuarios(correo, nombre, usuario, clave) VALUES(?,?,?,?)' ,(correo,nombre,usuario,clave,))
            cnn.commit()
            cnn.close()

        except Error as e:
            print (e)
        finally:
            if cnn:
                cnn.close()

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

def login(usuario, clave):
    if (find_user(usuario)==1):
        try:
            
            #coneccion a la db, la crea si no existe
            cnn = conection(db_file)
            cur = cnn.cursor()
            cur.execute("SELECT * FROM Usuarios WHERE Usuario=?", (usuario,))
            rows = cur.fetchall()
            print ("Tamaño de respuesta: ", len(rows))
            for row in rows:
                print(row[3]) ##ESTA ES LA CLAVE A COMPARAR

            if (clave == row[3]):
                print("La clave coincide")
            else:
                print ("La clave no coincide")
            #hacer login
            
            cnn.commit()
            cnn.close()

        except Error as e:
            print (e)
        finally:
            if cnn:
                cnn.close()
    else:
        print ("el usuario no existe")


conn = conection(db_file)
sql_create_users_table = """

CREATE TABLE IF NOT EXISTS Usuarios (
	Correo	INTEGER,
	Nombre	INTEGER,
	Usuario	INTEGER,
	Clave	INTEGER
);"""

if conn is not None:
        # create projects table
        create_table(conn, sql_create_users_table)
        
        registro("j@gmail.com","jorge","jazmitia","prueba")
else:
    print("Error! cannot create the database connection.")

login("jazmitia","prueba")
