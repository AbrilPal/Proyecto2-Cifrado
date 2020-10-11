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

def registro(correo, nombre, usuario, clave):
    try: 
        #coneccion a la db, la crea si no existe
        cnn = conection(db_file)
        
        #insert registro
        
        cnn.commit()
        cnn.close()

    except Error as e:
        print (e)
    finally:
        if cnn:
            cnn.close()


def login(usuario, clave):
    try: 
        #coneccion a la db, la crea si no existe
        cnn = conection(db_file)
        
        #hacer login
        
        cnn.commit()
        cnn.close()

    except Error as e:
        print (e)
    finally:
        if cnn:
            cnn.close()