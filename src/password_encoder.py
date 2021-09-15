import bcrypt

def encode_password(password):
    hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
    return hashed_password

def check_password(password, in_password):
    if bcrypt.checkpw(in_password, password):
        print("decrypted password")
    else:
        print("fuck u")
