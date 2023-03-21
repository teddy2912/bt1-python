import pandas as pd
from mysql.connector import MySQLConnection
import mysql.connector

db_config = {
    'host': 'localhost',
    'database': 'example-3',
    'user': 'root',
    'password': ''
}

file = pd.read_excel('input.xlsx', sheet_name='MAU', usecols='A:H', skiprows=10, nrows=52)
data = []
for row in file.iterrows():
    row_data = []
    for value in row[1]:
        row_data.append(value)
    sql = "insert into students(id, masv, first_name, last_name, birthday, toan, ly, hoa) values (%s,%s,%s,%s,%s,%s,%s,%s)"

    val = (row_data[0], row_data[1], row_data[2], row_data[3], row_data[4], row_data[5], row_data[6], row_data[7])
    cursor = db_config.cursor()
    cursor.execute(sql, val)
    db_config.commit()
    data.append(row_data)

myconn = mysql.connector.connect(host="localhost", user="root",
                                 password="", database="example-3")

cursor = myconn.cursor()


def select():
    cursor.execute("select * from students")
    result = cursor.fetchall()
    for x in result:
        print(x)


def insert():
    sql = "insert into students(id, masv, first_name, last_name, birthday, toan, ly, hoa)" + "values (%s,%s,%s,%s,%s,%s,%s,%s)"
    val = (55, "1", "Nguyen", "Hieu", "14/08/2002", 10, 10, 10)
    try:
        cursor.execute(sql, val)
        myconn.commit()
        print(cursor.rowcount, "inserted")
    except:
        myconn.rollback()
        myconn.close()


def update():
    try:
        cursor.execute("update students set first_name = 'Tran Van', last_name = 'An' where id = 54")
        myconn.commit()
        print(cursor.rowcount, "updated")
    except:
        myconn.rollback()
    myconn.close()


def delete():
    try:
        cursor.execute("delete from students where id = 53")
        myconn.commit()
        print(cursor.rowcount, "deleted")
    except:
        myconn.rollback()
        myconn.close()