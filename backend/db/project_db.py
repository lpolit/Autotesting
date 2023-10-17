import sqlite3

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


def create_table_project():
    execute('''CREATE TABLE projects
                   (id INT,"project_name", "date", "state", "user")''')

def insert_project(ProjectSchema):
    proximo_id = get_id_max()+1
    execute(f"INSERT INTO projects VALUES ({proximo_id},'{ProjectSchema.project_name}','{ProjectSchema.date}','{ProjectSchema.state}','{ProjectSchema.user}')")
    return proximo_id;

def update_project(ProjectSchema, project_id):
    execute(f"UPDATE projects SET project_name='{ProjectSchema.project_name}', date='{ProjectSchema.date}' WHERE id={project_id}")
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
    execute(f"DELETE FROM projects WHERE id = {id_project}")
    return id_project


def delete_all_projects():
    execute(f"DELETE FROM projects")

def get_id_max():
    con = sqlite3.connect(_DB)
    cur = con.cursor()
    cur.execute(f"SELECT MAX(id) FROM projects")
    project = cur.fetchone()
    con.close()
    return project[0]


def insert_inicial():
    execute(f"INSERT INTO projects VALUES (1,'Proyecto1','-','-','prueba@example.com')")