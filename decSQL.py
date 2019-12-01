import sqlite3

def commit_after_execute(con):
    def fun2(fun1):
        def wrapper(*args,**kwargs):
            return fun1(*args,**kwargs)
        con.commit()
        return wrapper
    return fun2

con = sqlite3.connect(':memory:')
cursorObj = con.cursor()
cursorObj.execute("CREATE TABLE table1(id integer PRIMARY KEY, name text)")
cursorObj.execute("INSERT INTO table1 VALUES(1, 'John')")
con.commit()

@commit_after_execute(con)
def sql_insert(entities):
    cursorObj = con.cursor()
    cursorObj.execute('INSERT INTO table1(id, name) VALUES(?, ?)', entities)

entities = (2, 'Andrew')
sql_insert(entities)
cursorObj.execute('SELECT * FROM table1')
rows = cursorObj.fetchall()
for row in rows:
    print(row)
