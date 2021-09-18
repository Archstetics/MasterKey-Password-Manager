import psycopg2
import password_crypt_hash
import clipboard

def connect_to_db():
    connection = psycopg2.connect(host="localhost", database="accounts", user="postgres", password="0306")
    return connection

def insert_new_account(account, userid, passwd, site_url, connection):
    try:
        cursor = connection.cursor()
        insert_query = """INSERT INTO uservault (account, userid, passwd, site_url) VALUES (%s, %s, %s, %s)"""
        records = (account, userid, passwd, site_url)
        cursor.execute(insert_query, records)
        connection.commit()
        print('\n', '-----------------------------------------------------', '\n')
        print(' Account entered.')
        print('\n', '-----------------------------------------------------', '\n')
    except (Exception, psycopg2.Error) as error:
        print(error)

def print_table(connection):
    try:
        cursor = connection.cursor()
        selection_query = """SELECT account, userid, site_url FROM uservault"""
        cursor.execute(selection_query)
        connection.commit()
        record = cursor.fetchall()
        print('\n', '-----------------------------------------------------', '\n')
        for i in range(len(record)):
            columns = record[i]
            for j in range(len(columns)):
                titles = [' Account:',' Username:',' URL:']
                print(titles[j], columns[j])
            print('\n', '-----------------------------------------------------', '\n')
    except (Exception, psycopg2.Error) as error:
        print(error)

def get_user_id_password(account, connection):
    try:
        cursor = connection.cursor()
        get_password_query = """SELECT userid, passwd FROM uservault WHERE account = '""" + account + "'"
        cursor.execute(get_password_query, account)
        connection.commit()
        record = cursor.fetchone()
        password = password_crypt_hash.decrypt_password(record[1].encode('utf-8'), password_crypt_hash.master_password_hashed)
        clipboard.copy(password.decode())
        print('\n', '-----------------------------------------------------', '\n')
        print(' Your username is:', record[0])
        print(' Your password is:', password.decode())
        print(' The password has been copied to the clipboard.')
        print('\n', '-----------------------------------------------------', '\n')
    except (Exception, psycopg2.Error) as error:
        print(error)

def reset_url(site_url, account, connection):
    try:
        cursor = connection.cursor()
        insert_query = """UPDATE uservault SET site_url = %s WHERE account = %s"""
        records = (site_url, account)
        cursor.execute(insert_query, records)
        connection.commit()
        print('\n', '-----------------------------------------------------', '\n')
        print(' URL modified.')
        print('\n', '-----------------------------------------------------', '\n')
    except (Exception, psycopg2.Error) as error:
        print(error)

def reset_account(new_account, account, connection):
    try:
        cursor = connection.cursor()
        insert_query = """UPDATE uservault SET account = %s WHERE account = %s"""
        records = (new_account, account)
        cursor.execute(insert_query, records)
        connection.commit()
        print('\n', '-----------------------------------------------------', '\n')
        print(' The account name has been modified.')
        print('\n', '-----------------------------------------------------', '\n')
    except (Exception, psycopg2.Error) as error:
        print(error)

def reset_user_id(new_user_id, account, connection):
    try:
        cursor = connection.cursor()
        insert_query = """UPDATE uservault SET userid = %s WHERE account = %s"""
        records = (new_user_id, account)
        cursor.execute(insert_query, records)
        connection.commit()
        print('\n', '-----------------------------------------------------', '\n')
        print(' Username modified')
        print('\n', '-----------------------------------------------------', '\n')
    except (Exception, psycopg2.Error) as error:
        print(error)

def reset_password(passwd, account, connection):
    try:
        cursor = connection.cursor()
        insert_query = """UPDATE uservault SET passwd = %s WHERE account = %s"""
        records = (passwd, account)
        cursor.execute(insert_query, records)
        connection.commit()
        print('\n', '-----------------------------------------------------', '\n')
        print(' Password modified.')
        print('\n', '-----------------------------------------------------', '\n')
    except (Exception, psycopg2.Error) as error:
        print(error)

def delete_account(account, connection):
    try:
        cursor = connection.cursor()
        deletion_query = """DELETE FROM uservault WHERE account = '""" + account + "'"
        cursor.execute(deletion_query, account)
        connection.commit()
        print('\n', '-----------------------------------------------------', '\n')
        print(' Account', account, 'has been deleted.')
        print('\n', '-----------------------------------------------------', '\n')
    except (Exception, psycopg2.Error) as error:
        print(error)