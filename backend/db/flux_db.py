import sqlite3

from common.file_utils import FileUtils

_DB = FileUtils.config_location()+"/autotesting.db"
def create_table_flux():
    con = sqlite3.connect(_DB)
    cur = con.cursor()
    # Create table
    cur.execute('''CREATE TABLE flujos
                   (nombre, flujo)''')
    con.commit()
    con.close()

def save_flux(FluxSchema):
    con = sqlite3.connect(_DB)
    cur = con.cursor()
    try:
        cur.execute(f"SELECT * FROM flujos WHERE nombre='{FluxSchema.name}'")
        cur.execute(f"UPDATE flujos SET flujo='{FluxSchema.flux}' WHERE nombre = '{FluxSchema.name}'")
    except:
        cur.execute(f"INSERT INTO flujos VALUES ('{FluxSchema.name}','{FluxSchema.flux}')")
    finally:
        con.commit()
        con.close()


def get_flux(name):
    con = sqlite3.connect(_DB)
    cur = con.cursor()
    cur.execute(f"SELECT * FROM flujos WHERE nombre='{name}'")
    flux =cur.fetchone()
    con.close()
    return flux

def get_all_flujos():
    con = sqlite3.connect(_DB)
    cur = con.cursor()
    cur.execute(f"SELECT * FROM flujos")
    fluxs = cur.fetchall()
    con.close()
    return fluxs
