import psycopg2
import db_manager
import argparse
import getpass

def main():
   # parser = argparse.ArgumentParser(description='MasterKey Password Manager: Generate secure password, .')
    
    connection = db_manager.connect_to_db()
    account = "Instagram"
    
    db_manager.get_user_id(account, connection)
    
    """
    account = input("Inserisci il nome del servizio (es. Facebook, Instagram): ")
    userid = input("Inserisci lo username: ")
    passwd = input("Inserisci la password: ")
    site_url = input("Inserisci l'URL del sito (es. www.facebook.com, www.instagram.com): ")
    
    
    db_manager.insert_new_account(account, userid, passwd, site_url, connection)
    """
    

main()