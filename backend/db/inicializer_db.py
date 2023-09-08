from db.user_db import create_table_users
from db.flux_db import create_table_flux


def inicializer_db():
    create_table_users()
    #create_table_flux()

if __name__ == "__main__":
    inicializer_db()

