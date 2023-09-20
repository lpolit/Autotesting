import sqlite3

from common.file_utils import FileUtils

_DB = FileUtils.config_location()+"/autotesting.db"
def create_table_flux():
    con = sqlite3.connect(_DB)
    cur = con.cursor()
    # Create table
    cur.execute('''CREATE TABLE fluxs
                   (id INT,"flux_name", "date", "state", "user", "flux", id_project)''')
    con.commit()
    con.close()


def insert_flux(FluxSchema):
    con = sqlite3.connect(_DB)
    cur = con.cursor()
    cur.execute(
        f"INSERT INTO fluxs VALUES ('{FluxSchema.id}','{FluxSchema.flux_name}','{FluxSchema.date}', '{FluxSchema.state}', '{FluxSchema.user}', '{FluxSchema.flux}','{FluxSchema.id_project}',)")
    con.commit()
    con.close()

def edit_flux(FluxSchema):
    con = sqlite3.connect(_DB)
    cur = con.cursor()
    try:
        cur.execute(
                f"UPDATE flujos SET flux='{FluxSchema.flux}' WHERE id = '{FluxSchema.id}'")
    except:
        print("FALLO AL INTENTAR INSERTAR O UPDATEAR EL FLUJO")
    finally:
        con.commit()
        con.close()


def get_flux(FluxSchema):
    con = sqlite3.connect(_DB)
    cur = con.cursor()
    cur.execute(f"SELECT * FROM fluxs WHERE flux_name='{FluxSchema.name}' and user ='{FluxSchema.user}'")
    flux =cur.fetchone()
    con.close()
    return flux

def get_fluxs_from_project(FluxSchema):
    con = sqlite3.connect(_DB)
    cur = con.cursor()
    cur.execute(f"SELECT * FROM fluxs WHERE id_project='{FluxSchema.id_project}'")
    fluxs =cur.fetchall()
    con.close()
    return fluxs


def get_all_flujos():
    con = sqlite3.connect(_DB)
    cur = con.cursor()
    cur.execute(f"SELECT * FROM fluxs")
    fluxs = cur.fetchall()
    con.close()
    return fluxs

def delete_all_flujos():
    con = sqlite3.connect(_DB)
    cur = con.cursor()
    cur.execute(f"DELETE FROM fluxs")
    con.commit()
    con.close()

