import hashlib

coder = hashlib.sha256()

def hash_password(password: str):
    coder.update(password.encode(encoding="utf-8"))
    return coder.hexdigest()