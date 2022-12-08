import hashlib
from cryptography.fernet import Fernet
from base64 import b64encode


class Crypto:
    def __init__(self):