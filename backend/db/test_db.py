import sqlite3

from common.file_utils import FileUtils


def test_db():
    con = sqlite3.connect(FileUtils.config_location()+"/autotesting.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE movie(title, year, score)")
    cur.execute("""
        INSERT INTO movie VALUES
            ('Monty Python and the Holy Grail', 1975, 8.2),
            ('And Now for Something Completely Different', 1971, 7.5)
    """)


    res = cur.execute("SELECT score FROM movie")

    print("acaaaaaaaaaaaaaaa")
    print(res.fetchall())
    con.close()