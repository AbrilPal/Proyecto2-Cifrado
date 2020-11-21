import sqlite3
from sqlite3 import Error
import binascii, os,base64,cifrado
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
    conn = conection(db_file)
    sql_create_users_table = """
 CREATE TABLE IF NOT EXISTS Usuarios (
 	Correo	TEXT,
 	Nombre	TEXT,
 	Usuario	TEXT,
 	Clave	TEXT
 );"""
    create_table(conn, sql_create_users_table)

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
                hashClave=cifrado.hash_Sha256(clave)
                if (hashClave == row[3]):
                    print("La clave coincide")
                    return "ok"
                else:
                    print ("La clave no coincide")
                    return "fail"
                 #hacer login
                cnn.commit()
                cnn.close()
        except Error as e:
             print (e)
        finally:
            if cnn:
                cnn.close()
  
    else:
        print ("El usuario no existe, intente de nuevo")
        return "fail"        
            

def setRegistro(nombres,apellidos,usuario,clave):
   
    print('parametros de setRegistro desde db.py------------------------------->')
    print(nombres)
    print(apellidos)
    print(usuario)
    print(clave)
    conn = conection(db_file)
    sql_create_users_table = """
 CREATE TABLE IF NOT EXISTS Usuarios (
 	Correo	TEXT,
 	Nombre	TEXT,
 	Usuario	TEXT,
 	Clave	TEXT
 );"""
    create_table(conn, sql_create_users_table)
    if (find_user(usuario)==1):
        print ("El usuario ya existe, ingrese otro")
        return "fail"
    else:
              
        try: 
            #coneccion a la db, la crea si no existe
            cnn = conection(db_file)
            #insert registro
            cur = cnn.cursor()
            hashClave=cifrado.hash_Sha256(clave)
            cur.execute('INSERT INTO Usuarios(correo, nombre, usuario, clave) VALUES(?,?,?,?)' ,(nombres,apellidos,usuario,hashClave,))
            cnn.commit()
            cnn.close()
            print("Usuario registrado satisfactoriamente")
        except Error as e:
            print (e)

        finally:
            if cnn:
                cnn.close()
                return "ok"


def setRegistrarDoc(hashdoc):
    print('parametros de setRegistrarDoc desde db.py------------------------------->')
    print(hashdoc)
    base = "AA"
    fin = "d"
    
    conn = conection(db_file)
    sql_create_docs_table = """
 CREATE TABLE IF NOT EXISTS Docs (
 	Hash	TEXT,
 	ID	TEXT
 );"""
    create_table(conn, sql_create_docs_table)
    print ("table created")
    ID = base64.b64encode(os.urandom(6)).decode('ascii')
    try:
        #coneccion a la db, la crea si no existe
        cnn = conection(db_file)
        #insert registro
        cur = cnn.cursor()
        cur.execute('INSERT INTO Docs(Hash, ID) VALUES(?,?)' ,(hashdoc,ID,))
        cnn.commit()
        cnn.close()
        print("Usuario registrado satisfactoriamente")
    except Error as e:
        print (e)

    finally:
        if cnn:
            cnn.close()
            return ID

    
    #cuando se registra en la db hay que retornar el codigo de la 
    #db asociado al hash para poder buscarlo despues
    return ('AA01s')

def getValidarDoc(hashdoc, codigo):
    print('parametros de getValidarDoc desde db.py------------------------------->')
    print(hashdoc)
    print(codigo)

    conn = conection(db_file)
    sql_create_docs_table = """
 CREATE TABLE IF NOT EXISTS Docs (
 	Hash	TEXT,
 	ID	TEXT
 );"""
    create_table(conn, sql_create_docs_table)

    try:
            
        #coneccion a la db, la crea si no existe
        cnn = conection(db_file)
        cur = cnn.cursor()
        cur.execute("SELECT * FROM Docs WHERE ID=?", (codigo,))
        rows = cur.fetchall()
        print ("Tamaño de respuesta: ", len(rows))
        for row in rows:
            print(row[0]) ##ESTA ES EL HASH A COMPARAR
            if (hashdoc == row[0]):
                print("el hash  coincide")
                return (True)
            else:
                print ("el hash no coincide")
                return (False)
               #hacer login
            cnn.commit()
            cnn.close()
    except Error as e:
            print (e)
    finally:
        if cnn:
            cnn.close()


    #cuando valida que el hash del codigo ingresado sea el hash de la db entonces
    #se retorna true or false
   
