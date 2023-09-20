from db.user_db import create_table_users, delete_all_users, get_all_users
from db.flux_db import create_table_flux, get_all_flujos, get_flux
from db.project_db import create_table_project, insert_inicial, get_id_max


def inicializer_db():
    create_table_users()
    create_table_flux()
    create_table_project()

if __name__ == "__main__":
    #inicializer_db()
    print(delete_all_users())

