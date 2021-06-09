import sqlite3

dbFile = 'app/db/chinook.db'


def ensure_connection(func):
    def inner(*args, **kwargs):
        with sqlite3.connect(dbFile) as conn:
            kwargs['conn'] = conn
            res = func(*args, **kwargs)
        return res
    return inner



@ensure_connection
def select_all(conn):
    c = conn.cursor()
    c.execute('SELECT * FROM employees')
    return c.fetchall()[0]



@ensure_connection
def select_names_tables(conn):
    c = conn.cursor()
    c.execute('PRAGMA table_info(employees)')
    return [i[1] for i in c.fetchall()]

if __name__ == '__main__':
    dbFile = 'chinook.db'
    data = select_all()
    print(data)


