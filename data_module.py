import sqlite3
from config import DB


def get_deputies():
    con = sqlite3.connect(DB)
    cur = con.cursor()
    cur.execute(''' SELECT tg_id, name, birthday, position, department, phone, email
                    FROM deputy_ministers''')
    deputies = cur.fetchall()
    con.close()
    return deputies
