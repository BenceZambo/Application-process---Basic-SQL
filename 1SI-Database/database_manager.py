from CONSTANTS import *
import psycopg2


def database_manager(query):
    connect_str = "dbname={0} user={1} host={2} password={3}".format(DBNAME, USERNAME, HOST, PASSWORD)
    conn = psycopg2.connect(connect_str)
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    return rows
