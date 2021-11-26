import sqlite3

con = sqlite3.connect('coffee.sqlite')
cur = con.cursor()


def get_all():
    return cur.execute('select table_.id, table_.name, types.name, table_.description, table_.price, table_.volume '
                       'from table_, types where table_.type=types.id').fetchall()
