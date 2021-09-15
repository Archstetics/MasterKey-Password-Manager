import psycopg2
import db_manager
import password_generator
import argparse
import getpass

def print_hi():
    print("hi")

def main():
    parser = argparse.ArgumentParser(description='MasterKey Password Manager: generate secure password, store and manage all your account credentials.')
    connection = db_manager.connect_to_db()

    parser.add_argument('-a', '--add', type=str, nargs=4, help='Add new account.', metavar=("[ACCOUNT]", "[USERID]", "[PASSWD]", "[SITE_URL]"))
    parser.add_argument('-l', '--list', help='List all registered accounts')
    parser.add_argument('-gp', '--get_password', type=str, nargs=1, help='Search password by selecting the service account', metavar=("[ACCOUNT]"))
    parser.add_argument('-gu', '--get_username', type=str, nargs=1, help='Search username by selecting the service account', metavar=("[ACCOUNT]"))
    parser.add_argument('-ra', '--reset_account', type=str, nargs=1, help='Reset service account name', metavar=("[ACCOUNT]"))
    parser.add_argument('-ru', '--reset_username', type=str, nargs=1, help='Reset username', metavar=("[ACCOUNT]"))
    parser.add_argument('--rp', '--reset_password', type=str, nargs=1, help='Reset password', metavar=("[ACCOUNT]"))
    parser.add_argument('--rl', '--reset_url', type=str, nargs=1, help='Reset Url', metavar=("[ACCOUNT]"))

    args = parser.parse_args()


main()