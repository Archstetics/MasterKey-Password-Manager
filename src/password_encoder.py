import bcrypt

###############################################################################################################
# REMINDER:
#
# Criptare password database
###############################################################################################################

def encode_password(password):
    hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
    return hashed_password

def check_master_password(input_master_password):
    master_password_hashed = "$2a$12$U3ClBLe7P0nWrzri2/R10O7FBUfKBxobITq4JSudOKME.ahJy45HG"
    return bcrypt.checkpw(input_master_password, master_password_hashed)

