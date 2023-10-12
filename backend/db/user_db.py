import sqlite3

from common.file_utils import FileUtils

_DB = FileUtils.config_location()+"/autotesting.db"
def create_table_users():
    con = sqlite3.connect(_DB)
    cur = con.cursor()
    # Create table
    cur.execute('''CREATE TABLE usuarios
                   (nombre, email, password)''')
    con.commit()
    con.close()

def insert_user(UserSchema):
    con = sqlite3.connect(_DB)
    cur = con.cursor()
    cur.execute(f"INSERT INTO usuarios VALUES ('{UserSchema.fullname}','{UserSchema.email}','{UserSchema.password}')")
    con.commit()
    con.close()


def get_user(email : str):
    con = sqlite3.connect(_DB)
    cur = con.cursor()
    usu = cur.execute(f"SELECT * FROM usuarios WHERE email={email}")
    con.close()
    return usu

def get_all_users():
    con = sqlite3.connect(_DB)
    cur = con.cursor()
    cur.execute(f"SELECT * FROM usuarios")
    usus = cur.fetchall()
    con.close()
    return usus

def delete_all_users():
    con = sqlite3.connect(_DB)
    cur = con.cursor()
    cur.execute(f"DELETE FROM usuarios")
    con.commit()
    con.close()

def change_password_user(user, password='123456'):
    con = sqlite3.connect(_DB)
    cur = con.cursor()
    try:
        cur.execute(f"UPDATE usuarios SET password='{password}' WHERE email='{user}'")
    except:
        print("FALLO EL CAMBIO DE LA CONTRASEÑA")
    finally:
        con.commit()
        con.close()
    return user;
