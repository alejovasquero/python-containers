import uuid
import hashlib


def sha_hash_salt(password):
    salt = uuid.uuid4().hex
    return hash(hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt)


def salt_hash(value):
    return hash("salt123" + str(value))


def normal_hash(value):
    return hash(value)
