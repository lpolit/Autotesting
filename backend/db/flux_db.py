import json
import sqlite3

from common.file_utils import FileUtils

_DB = FileUtils.config_location()+"/autotesting.db"
def create_table_flux():
    con = sqlite3.connect(_DB)
    cur = con.cursor()
    # Create table
    cur.execute('''CREATE TABLE fluxs
                   (id INT,"flux_name", "date", "state", "user", "flux", id_project INT)''')
    con.commit()
    con.close()


def insert_flux(FluxSchema):
    con = sqlite3.connect(_DB)
    cur = con.cursor()
    proximo_id = get_id_max()+1
    cur.execute(
        f"INSERT INTO fluxs VALUES ({proximo_id},'{FluxSchema.flux_name}','{FluxSchema.date}', '{FluxSchema.state}', '{FluxSchema.user}', '{FluxSchema.flux}',{int(FluxSchema.project_id)})")
    con.commit()
    con.close()
    return proximo_id

def update_name_flux(flux_name, flow_id):
    con = sqlite3.connect(_DB)
    cur = con.cursor()
    try:
        cur.execute(
                f"UPDATE fluxs SET flux_name='{flux_name}' WHERE id = {int(flow_id)}")
    except:
        print("FALLO AL INTENTAR INSERTAR O UPDATEAR EL FLUJO")
    finally:
        con.commit()
        con.close()

def update_flux(FluxSchema, flow_id):
    con = sqlite3.connect(_DB)
    cur = con.cursor()
    try:
        cur.execute(
                f"UPDATE fluxs SET flux='{FluxSchema.flux}' WHERE id = {int(flow_id)}")
    except:
        print("FALLO AL INTENTAR INSERTAR O UPDATEAR EL FLUJO")
    finally:
        con.commit()
        con.close()


def get_flux(id_flux):
    con = sqlite3.connect(_DB)
    cur = con.cursor()
    cur.execute(f"SELECT * FROM fluxs WHERE id='{id_flux}'")
    flux =cur.fetchone()
    con.close()
    return flux

def get_all_fluxs():
    con = sqlite3.connect(_DB)
    cur = con.cursor()
    cur.execute(f"SELECT * FROM fluxs")
    fluxs =cur.fetchall()
    con.close()
    return fluxs


def get_fluxs_from_project(project_id):
    con = sqlite3.connect(_DB)
    cur = con.cursor()
    cur.execute(f"SELECT * FROM fluxs WHERE id_project = {project_id}")
    fluxs = cur.fetchall()
    con.close()
    return fluxs

def delete_flux(flux_id: int):
    con = sqlite3.connect(_DB)
    cur = con.cursor()
    cur.execute(f"DELETE FROM fluxs WHERE id = {flux_id}")
    con.commit()
    con.close()
    return flux_id

def delete_all_flujos():
    con = sqlite3.connect(_DB)
    cur = con.cursor()
    cur.execute(f"DELETE FROM fluxs")
    con.commit()
    con.close()

def get_id_max():
    con = sqlite3.connect(_DB)
    cur = con.cursor()
    cur.execute(f"SELECT MAX(id) FROM fluxs")
    flux = cur.fetchone()
    con.close()
    return flux[0] if flux[0] != None else 0

