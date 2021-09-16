import db_manager
import password_crypt_hash
import password_generator
import getpass
import sys
from os import system
from PyInquirer import prompt


def master_password_init(questions):
    answer = prompt(questions[0])

    if answer['pass'] == 'yes':
        return 0   
    else:
        answer = prompt(questions[1])

        if answer['generate'] == 'I choose it':
            new_master_password_input = getpass.getpass("Enter your new master password: ")
            hashed_password = password_crypt_hash.encode_password(new_master_password_input)
            print("Your new master password is: ", new_master_password_input)
            print("Your hashed master password is: ", hashed_password)
            print("Enter your hashed master password in password_crypt_hash.py and run the program again.")
            sys.exit()

        elif answer['generate'] == 'generate it automatically':
            lenght = int(input("Enter the password length: "))
            password = password_crypt_hash.generate_password_digit_punct(lenght)
            hashed_password = password_crypt_hash.encode_password(password)
            print("Your new master password is: ", password)
            print("Your hashed master password is: ", hashed_password)
            print("Enter your hashed master password in password_crypt_hash.py and run the program again.")
            sys.exit()

def login():
    master_password_input = getpass.getpass("Login with your master password: ")
    if password_crypt_hash.check_master_password(master_password_input) == True:
        connection = db_manager.connect_to_db()
        print("Sucessfully Authenticated.")
        return connection
    else:
        print("Authentication failed. Try to run the program again.")
        sys.exit()


def main():
    questions = [
    {
        'type': 'list',
        'name': 'pass',
        'message': 'Welcome, have you already set your hashed master password in password_encoder.py?',
        'choices': ['yes', 'no']
    },
    {
        'type': 'list',
        'name': 'generate',
        'message': 'Do you prefer to have your password generated by the program or do you want to create it yourself?',
        'choices': ['I choose it', 'generate it automatically']
    },
    {
        'type': 'list',
        'name': 'menu',
        'message': 'Choose an option:',
        'choices': ['Add new account.',
            'List all registered accounts.',
            'Generate a secure password.', 
            'Search password by selecting the service account.',
            'Search username by selecting the service account.',
            'Reset service account name.',
            'Reset username.',
            'Reset password.',
            'Reset Url.'
            ]
    },
    {
        'type': 'list',
        'name': 'password',
        'message': 'Password details:',
        'choices': ['Characters only.',
            'Characters and numbers.',
            'Characters and special characters.', 
            'characters, numbers and special characters'
            ]
    }]
    
    master_password_init(questions)
    connection = login()
    answer = prompt(questions[2])

    if answer['menu'] == 'Add new account.':
        account = input('Enter the account service name: ')
        userid = input('Enter the username: ')
        passwd = getpass.getpass('Enter the password: ')
        site_url = input('Enter the URL: ')
        db_manager.insert_new_account(account, userid, passwd, site_url, connection)

    if answer['menu'] == 'List all registered accounts.':
        db_manager.print_table(connection)

    if answer['menu'] == 'Generate a secure password.':
        answer = prompt(questions[3])
        lenght = int(input("Enter the number of characters: "))

        if answer['password'] == 'Characters only.':
            password = password_generator.generate_password(lenght)

        if answer['password'] == 'Characters and numbers.':
            password = password_generator.generate_password_digit(lenght)

        if answer['password'] == 'Characters and special characters.':
            password = password_generator.generate_password_punct(lenght)

        if answer['password'] == 'Characters and special characters.':
            password = password_generator.generate_password_punct(lenght)  

        print('Your new secure password is: ', password)

    if answer['menu'] == 'Search password by selecting the service account.':
        account = input('Account name: ')
        db_manager.get_password(account, connection)

    if answer['menu'] == 'Search username by selecting the service account.':
        account = input('Account name: ')
        db_manager.get_user_id(account, connection)

    if answer['menu'] == 'Reset service account name.':
        account = input('Old account name: ')
        new_account = input('enter new account name: ')
        db_manager.reset_account(new_account, account, connection)

    if answer['menu'] == 'Reset username.':
        account = input('Account name: ')
        new_user_id = input('enter new username: ')
        db_manager.reset_user_id(new_user_id, account, connection)

    if answer['menu'] == 'Reset password.':
        account = input('Account name: ')
        new_passwd = input('enter new password: ')
        db_manager.reset_user_id(new_passwd, account, connection)

    if answer['menu'] == 'Reset Url.':
        account = input('Account name: ')
        new_url = input('enter new Url: ')
        db_manager.reset_user_id(new_url, account, connection)


main()