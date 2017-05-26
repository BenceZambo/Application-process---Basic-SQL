def mentors_nick_from_Miskolc():
    try:
        # setup connection string
        connect_str = "dbname='zambo' user='zambo' host='localhost' password='zambog'"
        # use our connection values to establish a connection
        conn = psycopg2.connect(connect_str)
        # set autocommit option, to do every query when we call it
        conn.autocommit = True
        # create a psycopg2 cursor that can execute queries
        cursor = conn.cursor()
        cursor.execute("""SELECT  nick_name FROM mentors WHERE city='Miskolc';""")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Exception as e:
        print("Uh oh, can't connect. Invalid dbname, user or password?")
        print(e)


def something_Carol():
    try:
        # setup connection string
        connect_str = "dbname='zambo' user='zambo' host='localhost' password='zambog'"
        # use our connection values to establish a connection
        conn = psycopg2.connect(connect_str)
        # set autocommit option, to do every query when we call it
        conn.autocommit = True
        # create a psycopg2 cursor that can execute queries
        cursor = conn.cursor()
        cursor.execute("""SELECT first_name, last_name, phone_number FROM applicants WHERE first_name = 'Carol';""")
        rows = cursor.fetchall()
        print(rows)
    except Exception as e:
        print("Uh oh, can't connect. Invalid dbname, user or password?")
        print(e)


def from_Adipiscingenimmi_University():
    try:
        # setup connection string
        connect_str = "dbname='zambo' user='zambo' host='localhost' password='zambog'"
        # use our connection values to establish a connection
        conn = psycopg2.connect(connect_str)
        # set autocommit option, to do every query when we call it
        conn.autocommit = True
        # create a psycopg2 cursor that can execute queries
        cursor = conn.cursor()
        cursor.execute("""SELECT first_name, last_name, phone_number FROM applicants
                        WHERE email LIKE '%@adipiscingenimmi.edu';""")
        rows = cursor.fetchall()
        print(rows)
    except Exception as e:
        print("Uh oh, can't connect. Invalid dbname, user or password?")
        print(e)


def insert_new_codecooler():
    try:
        # setup connection string
        connect_str = "dbname='zambo' user='zambo' host='localhost' password='zambog'"
        # use our connection values to establish a connection
        conn = psycopg2.connect(connect_str)
        # set autocommit option, to do every query when we call it
        conn.autocommit = True
        # create a psycopg2 cursor that can execute queries
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO applicants(first_name, last_name, phone_number, email, application_code)
                        #VALUES('Markus', 'Schaffarzyk', '003620/725-2666', 'djnovus@groovecoverage.com', 54823);""")
        cursor.execute("""SELECT * FROM applicants WHERE application_code = 54823;""")
        rows = cursor.fetchall()
        print(rows)
    except Exception as e:
        print("Uh oh, can't connect. Invalid dbname, user or password?")
        print(e)


def update_jemimas_phone():
    try:
        # setup connection string
        connect_str = "dbname='zambo' user='zambo' host='localhost' password='zambog'"
        # use our connection values to establish a connection
        conn = psycopg2.connect(connect_str)
        # set autocommit option, to do every query when we call it
        conn.autocommit = True
        # create a psycopg2 cursor that can execute queries
        cursor = conn.cursor()
        cursor.execute("""UPDATE applicants SET phone_number = '003670/223-7459'
                        WHERE first_name = 'Jemima' AND last_name = 'Foreman';""")
        cursor.execute("""SELECT phone_number FROM applicants
                         WHERE first_name = 'Jemima' AND last_name = 'Foreman';""")
        rows = cursor.fetchall()
        print(rows)
    except Exception as e:
        print("Uh oh, can't connect. Invalid dbname, user or password?")
        print(e)


def delete_some_applicants():
    try:
        # setup connection string
        connect_str = "dbname='zambo' user='zambo' host='localhost' password='zambog'"
        # use our connection values to establish a connection
        conn = psycopg2.connect(connect_str)
        # set autocommit option, to do every query when we call it
        conn.autocommit = True
        # create a psycopg2 cursor that can execute queries
        cursor = conn.cursor()
        cursor.execute("""DELETE FROM applicants WHERE email LIKE '%mauriseu.net';""")
    except Exception as e:
        print("These are already deleted!")
        print(e)