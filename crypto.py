import hashlib
from cryptography.fernet import Fernet
from base64 import b64encode


class Crypto:
    def __init__(self, pin):
        self.pin = Crypto.prepare_pin(pin)
        self.fernet = Fernet(self.pin)

    @staticmethod
    def prepare_pin(pin):

        
