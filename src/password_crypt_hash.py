import bcrypt
import base64
import hashlib
from Cryptodome import Random
from Cryptodome.Cipher import AES
from Cryptodome.Protocol.KDF import PBKDF2
###############################################################################################################
# REMINDER:
#
# Criptare password database
###############################################################################################################

BLOCK_SIZE = 16
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]


master_password_hashed = '$2a$12$U3ClBLe7P0nWrzri2/R10O7FBUfKBxobITq4JSudOKME.ahJy45HG'

def hash_master_password(password, salt):
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password

def check_master_password(input_master_password, master_password_hashed):
    # master_password_hashed = '$2a$12$U3ClBLe7P0nWrzri2/R10O7FBUfKBxobITq4JSudOKME.ahJy45HG'
    return bcrypt.checkpw(input_master_password.encode(), master_password_hashed.encode())

def get_private_key(master_password_hashed):
    salt = 'insert_your_salt_here'
    kdf = PBKDF2(master_password_hashed, salt, 64, 1000)
    key = kdf[:32]
    return key

def encrypt_password(password, master_password_hashed):
    key= get_private_key(master_password_hashed)
    return AES.new(key, AES.MODE_CBC, salt).encrypt(r_pad(password))

def decrypt_password(encrypted_password, master_password_hashed, length):
    key = get_private_key(master_password_hashed)
    private_key = get_private_key(master_password_hashed)
    encrypted_password = base64.b64decode(encrypted_password)
    iv = encrypted_password[:16]
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    password = unpad(cipher.decrypt(encrypted_password[16:])).decode()
    return password
    

password = 'ciaociao'

encrypted_password = encrypt_password(password, master_password_hashed)

print('the encrypted password is', encrypted_password)
print(type(encrypted_password))
#encrypted_password = str(encrypted_password)
#encrypted_password = bytes(encrypted_password, 'utf-8')

password = None

password = decrypt_password(encrypted_password, master_password_hashed)

print('the decrypted password is', password)
