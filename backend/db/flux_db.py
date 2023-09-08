import sqlite3
def create_table_flux():
    con = sqlite3.connect("autotesting.db")
    cur = con.cursor()
    # Create table

    cur.execute("CREATE TABLE movie(title, year, score)")


    con.commit()
    con.close()





def insert_flux(flux: str):
    con = sqlite3.connect("autotesting.db")
    cur = con.cursor()
    cur.execute("""
            INSERT INTO movie VALUES
                ('Monty Python and the Holy Grail', 1975, 8.2),
                ('And Now for Something Completely Different', 1971, 7.5)
        """)

    con.close()

def get_all_fluxs():
    con = sqlite3.connect("autotesting.db")
    cur = con.cursor()
    res = cur.execute("SELECT score FROM movie")
    print("acaaaaaaaaaaaaaaa")
    print(res.fetchall())