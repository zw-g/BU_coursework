import json
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from .. import constants


def check_comlexity_requirements(password: str):
    if not any(ch.isupper() for ch in password):
        raise RuntimeError('Password must include a capital letter')
    if not any(ch.islower() for ch in password):
        raise RuntimeError('Password must include a small letter')
    if not any(ch.isdigit() for ch in password):
        raise RuntimeError('Password must include a digit')
    if len(password) < constants.MIN_PASSWORD_LENGTH:
        raise RuntimeError(
            f'Password must be at least {constants.MIN_PASSWORD_LENGTH} characters long'
        )
    if len(password) > constants.MAX_PASSWORD_LENGTH:
        raise RuntimeError(
            f'Password must be at most {constants.MAX_PASSWORD_LENGTH} characters long'
        )


# Ref: https://cryptography.io/en/latest/fernet/#using-passwords-with-fernet
def encrypt(d: dict, encryption_key: bytes) -> bytes:
    d_str = json.dumps(d)
    return Fernet(encryption_key).encrypt(d_str.encode())


def decrypt(data: bytes, encryption_key: bytes) -> dict:
    d_str = Fernet(encryption_key).decrypt(data).decode()
    return json.loads(d_str)


def get_encryption_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))
