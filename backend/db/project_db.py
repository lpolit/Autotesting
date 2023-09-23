import sqlite3

from common.file_utils import FileUtils

_DB = FileUtils.config_location()+"/autotesting.db"
def create_table_project():
    con = sqlite3.connect(_DB)
    cur = con.cursor()
    # Create table
    cur.execute('''CREATE TABLE projects
                   (id INT,"project_name", "date", "state", "user")''')
    con.commit()
    con.close()

def insert_project(ProjectSchema):
    con = sqlite3.connect(_DB)
    cur = con.cursor()
    proximo_id = get_id_max()+1
    try:
        cur.execute(f"INSERT INTO projects VALUES ({proximo_id},'{ProjectSchema.project_name}','{ProjectSchema.date}','{ProjectSchema.state}','{ProjectSchema.user}')")
    except:
        print("FALLO AL INTENTAR INSERTAR O UPDATEAR EL PROYECTO")
    finally:
        con.commit()
        con.close()
    return proximo_id;

def update_project(ProjectSchema, project_id):
    con = sqlite3.connect(_DB)
    cur = con.cursor()
    try:
        cur.execute(f"UPDATE projects SET project_name='{ProjectSchema.project_name}', date='{ProjectSchema.date}' WHERE id={project_id}")
    except:
        print("FALLO AL UPDATEAR EL PROYECTO")
    finally:
        con.commit()
        con.close()
    return project_id;

def get_project(ProjectSchema):
    con = sqlite3.connect(_DB)
    cur = con.cursor()
    cur.execute(f"SELECT * FROM projects WHERE project_name='{ProjectSchema.name}' and user ='{ProjectSchema.user}'")
    project =cur.fetchone()
    con.close()
    return project



def get_all_projects():
    con = sqlite3.connect(_DB)
    cur = con.cursor()
    cur.execute(f"SELECT * FROM projects")
    projects = cur.fetchall()
    con.close()
    return projects

def get_all_projects_for_user(username):
    con = sqlite3.connect(_DB)
    cur = con.cursor()
    cur.execute(f"SELECT * FROM projects WHERE user = '{username}'")
    projects = cur.fetchall()
    con.close()
    return projects

def delete_project(id_project: int):
    con = sqlite3.connect(_DB)
    cur = con.cursor()
    cur.execute(f"DELETE FROM projects WHERE id = {id_project}")
    con.commit()
    con.close()
    return id_project


def delete_all_projects():
    con = sqlite3.connect(_DB)
    cur = con.cursor()
    cur.execute(f"DELETE FROM projects")
    con.commit()
    con.close()

def get_id_max():
    con = sqlite3.connect(_DB)
    cur = con.cursor()
    cur.execute(f"SELECT MAX(id) FROM projects")
    project = cur.fetchone()
    con.close()
    return project[0]


def insert_inicial():
    con = sqlite3.connect(_DB)
    cur = con.cursor()
    try:
        cur.execute(f"INSERT INTO projects VALUES (1,'Proyecto1','-','-','prueba@example.com')")
    except:
        print("FALLO AL INTENTAR INSERTAR O UPDATEAR EL PROYECTO")
    finally:
        con.commit()
        con.close()