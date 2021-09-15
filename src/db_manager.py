import psycopg2

def connect_to_db():
    try:
        # Set your PostgreSQL host, database, user and password between the quotes
        connection = psycopg2.connect(host="localhost", database="accounts", user="postgres", password="0306")
        return connection
    except (Exception, psycopg2.Error) as error:
        print(error)

def insert_new_account(account, userid, passwd, site_url, connection):
    try:
        cursor = connection.cursor()
        insert_query = """INSERT INTO uservault (account, userid, passwd, site_url) VALUES (%s, %s, %s, %s)"""
        records = (account, userid, passwd, site_url)
        cursor.execute(insert_query, records)
        connection.commit()
        print('Account inserito.')
    except (Exception, psycopg2.Error) as error:
        print(error)

def print_table(connection):
    try:
        cursor = connection.cursor()
        insert_query = """SELECT * FROM uservault"""
        cursor.execute(insert_query)
        connection.commit()
        record = cursor.fetchall()
        for i in range(len(record)):
            columns = record[i]
            for j in range(len(columns)):
                titles = ["Account: ","Username: ","Password: ","URL: "]
                print(titles[j], columns[j])
    except (Exception, psycopg2.Error) as error:
        print(error)

def get_password(account, connection):
    try:
        cursor = connection.cursor()
        get_password_query = """SELECT passwd FROM uservault WHERE account = '""" + account + "'"
        cursor.execute(get_password_query, account)
        connection.commit()
        record = cursor.fetchone()
        print('Password is: ',record[0])
    except (Exception, psycopg2.Error) as error:
        print(error)

def get_user_id(account, connection):
    try:
        cursor = connection.cursor()
        get_password_query = """SELECT userid FROM uservault WHERE account = '""" + account + "'"
        cursor.execute(get_password_query, account)
        connection.commit()
        record = cursor.fetchone()
        print('User ID is: ', record[0])
    except (Exception, psycopg2.Error) as error:
        print(error)

def reset_url(site_url, account, connection):
    try:
        cursor = connection.cursor()
        insert_query = """UPDATE uservault SET site_url = %s WHERE account = %s"""
        records = (site_url, account)
        cursor.execute(insert_query, records)
        connection.commit()
        print('URL modificato.')
    except (Exception, psycopg2.Error) as error:
        print(error)

def reset_account(new_account, account, connection):
    try:
        cursor = connection.cursor()
        insert_query = """UPDATE uservault SET account = %s WHERE account = %s"""
        records = (new_account, account)
        cursor.execute(insert_query, records)
        connection.commit()
        print("Il servizio dell'account è stato modificato")
    except (Exception, psycopg2.Error) as error:
        print(error)

def reset_account(userid, account, connection):
    try:
        cursor = connection.cursor()
        insert_query = """UPDATE uservault SET userid = %s WHERE account = %s"""
        records = (userid, account)
        cursor.execute(insert_query, records)
        connection.commit()
        print('Username modificato')
    except (Exception, psycopg2.Error) as error:
        print(error)

def reset_password(passwd, account, connection):
    try:
        cursor = connection.cursor()
        insert_query = """UPDATE uservault SET passwd = %s WHERE account = %s"""
        records = (passwd, account)
        cursor.execute(insert_query, records)
        connection.commit()
        print('Password modificata.')
    except (Exception, psycopg2.Error) as error:
        print(error)