import bcrypt

def create_password_hash(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

def check_password(password, hashed):
    return bcrypt.hashpw(password.encode(), hashed) == hashed