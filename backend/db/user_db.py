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
