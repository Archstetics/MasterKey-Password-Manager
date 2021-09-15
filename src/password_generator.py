import string
import random
import secrets

###############################################################################################################
# REMINDER:
#
# Aggiustare punctuation (usa solo !@#$%^&*)
# Cercare di utilizzare solo libreria secrets
###############################################################################################################

def generate_password(lenght):
    alphabet = string.ascii_letters
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(lenght))
        if (any(c.islower() for c in password) and any(c.isupper() for c in password)):
            break
    print(password)

def generate_password_digit(lenght):
    alphabet = string.ascii_letters + string.digits
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(lenght))
        if (any(c.islower() for c in password) and any(c.isupper() for c in password) and sum(c.isdigit() for c in password) >= 2):
            break
    print(password)

def generate_password_punct(lenght):
    alphabet = string.ascii_letters + string.punctuation
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(lenght))
        if (any(c.islower() for c in password)):
            break

        if not any(string.punctuation) in list(password):
            password = list(password)
            password.pop(random.randrange(lenght))
            password.insert(random.randrange(lenght), random.choice(string.punctuation))
            password = ''.join(password)
    print(password)

def generate_password_digit_punct(lenght):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(lenght))
        if (any(c.islower() for c in password) and any(c.isupper() for c in password) and sum(c.isdigit() for c in password) >= 2):
            break

        if not any(string.punctuation) in list(password):
            password = list(password)
            password.pop(random.randrange(lenght))
            password.insert(random.randrange(lenght), random.choice(string.punctuation))
            password = ''.join(password)
    print(password) 