import bcrypt
from base64 import b64encode, b64decode
from Cryptodome.Cipher import AES
from Cryptodome.Protocol.KDF import PBKDF2

master_password_hashed = '$2a$12$U3ClBLe7P0nWrzri2/R10O7FBUfKBxobITq4JSudOKME.ahJy45HG'

def hash_master_password(password):
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed_password.decode()

def check_master_password(input_master_password, master_password_hashed):
    return bcrypt.checkpw(input_master_password.encode(), master_password_hashed.encode())

def get_private_key(master_password_hashed):
    salt = 'insert_your_salt_here'
    kdf = PBKDF2(master_password_hashed, salt, 64, 1000)
    key = kdf[:32]
    return key

def encrypt_password(password_to_encrypt, master_password_hashed):
    key = get_private_key(master_password_hashed)
    password_to_encrypt = str.encode(password_to_encrypt)
    cipher = AES.new(key, AES.MODE_EAX)
    cipher_password, tag = cipher.encrypt_and_digest(password_to_encrypt)
    encrypted_password = b64encode(cipher_password + cipher.nonce).decode()
    return encrypted_password

def decrypt_password(encrypted_password, master_password_hashed):
    key = get_private_key(master_password_hashed)
    if len(encrypted_password) % 4:
        encrypted_password += '=' * (4 - len(encrypted_password) % 4)
    nonce = b64decode(encrypted_password)[-16:]
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    password = cipher.decrypt(b64decode(encrypted_password)[:-16])
    return password