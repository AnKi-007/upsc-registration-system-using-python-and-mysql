import mysql.connector as sql

def get_connection():
    return sql.connect(
        host='localhost',
        user='root',
        passwd='Db_JaiShreeRAM@01',
        database='UPSC'
    )
