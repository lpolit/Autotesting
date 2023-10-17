import json
import sqlite3
import time

from common.file_utils import FileUtils

_DB = FileUtils.config_location()+"/autotesting.db"


def execute(query: str):
    try:
        con = sqlite3.connect(_DB)
        cur = con.cursor()
        cur.execute(query)
    except Exception as e:
        print("Fallo la ejecucion con el error: "+e)
    finally:
        con.commit()
        con.close()

def create_table_flux():
    execute('''CREATE TABLE fluxs
                   (id INT,"flux_name", "date", "state", "user", "flux", id_project INT)''')


def insert_flux(FluxSchema):
   proximo_id = get_id_max()+1
   execute(f"INSERT INTO fluxs VALUES ({proximo_id},'{FluxSchema.flux_name}','{FluxSchema.date}', '{FluxSchema.state}', '{FluxSchema.user}', '{FluxSchema.flux}',{int(FluxSchema.project_id)})")
   return proximo_id

def update_name_flux(flux_name, flow_id):
    import json
    flux = get_flux(flow_id)
    flux = flux[5]
    if flux != ' ':
        flux_json = json.loads(flux)
        flux_json["flux_name"] = flux_name + "-" + flux_json["flux_name"].split("-")[1]
        flux = json.dumps(flux_json)

    execute(f"UPDATE fluxs SET flux_name='{flux_name}', flux= '{flux}' WHERE id = {int(flow_id)}")


def update_flux(FluxSchema, flow_id):
    execute(f"UPDATE fluxs SET flux='{FluxSchema.flux}' WHERE id = {int(flow_id)}")

def update_date(flow_id):
    date = time.strftime("%x") + " " + time.strftime("%X")
    execute(f"UPDATE fluxs SET date='{date}' WHERE id = {int(flow_id)}")
    return date


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
    execute(f"DELETE FROM fluxs WHERE id = {flux_id}")
    return flux_id

def delete_all_flujos():
    execute(f"DELETE FROM fluxs")

def get_id_max():
    con = sqlite3.connect(_DB)
    cur = con.cursor()
    cur.execute(f"SELECT MAX(id) FROM fluxs")
    flux = cur.fetchone()
    con.close()
    return flux[0] if flux[0] != None else 0

