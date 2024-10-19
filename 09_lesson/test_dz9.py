import pytest
import requests

from sqlalchemy import create_engine
from sqlalchemy import text

db_connection_string = 'postgresql://postgre:qwe@localhost:5432/postgres'

def test_select():

    db = create_engine(db_connection_string)
    rows = db.execute("select * from subject").fetchall()
    row1 = rows[0]

assert row1["subject_title"] == 'English'

def test_insert():

    db = create_engine(db_connection_string)
    db.execute('''INSERT into subject (subject_id, subject_title) VALUES(17, 'Alchemy');''')
    rows = db.execute("select * from subject").fetchall()
    row_1=rows[-1]
    sql = text("DELETE FROM subject WHERE subject_id = :id")
    db.execute(sql, id=17)

assert row1["subject_title"] == 'Alchemy'

def test_update():
 
    db = create_engine(db_connection_string)
    db.execute('''INSERT into subject (subject_id, subject_title) VALUES(17, 'Alchemy');''')
    rows = db.execute("select * from subject").fetchall()
    row1=rows[-1]
    sql = text("update subject set subject_title = :new_title where subject_id=:id")
    db.execute(sql, new_title = 'Alchemy2', id = row1["subject_id"])
    rows = db.execute("select * from subject").fetchall()
    row2=rows[-1]
    sql = text("DELETE FROM subject WHERE subject_id = :id")
    id_update = row2["subject_id"]
    db.execute(sql, id=id_update)

assert rows["subject_title"] == "Alchemy2"

def test_delete():

    db = create_engine(db_connection_string)
    db.execute('''INSERT into subject (subject_id, subject_title) VALUES(17, 'Alchemy');''')
    rows = db.execute("select * from subject").fetchall()
    row1=rows[-1]
    sql = text("DELETE FROM subject WHERE subject_id = :id")
    db.execute(sql, id=17)

assert row1["name"] == name
