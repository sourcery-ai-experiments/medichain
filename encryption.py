import json
from typing import Any

from cryptography.fernet import Fernet, InvalidToken


class CryptographyHelper:
    def __init__(self, key: bytes = None):
        self.key = Fernet.generate_key() if key is None else key
        self.cipher_suite = Fernet(self.key)

    def encrypt_data(self, data: Any) -> str:
        serialized_data = str(data).encode()
        encrypted_data = self.cipher_suite.encrypt(serialized_data)
        return encrypted_data.decode()

    def decrypt_data(self, encrypted_data: str) -> str:
        decrypted_data = self.cipher_suite.decrypt(encrypted_data.encode())
        return decrypted_data.decode()

    def get_key(self) -> str:
        return self.key.decode()


class CryptographyManager:
    def __init__(self):
        self.keys = {}

    def encrypt_item(self, item_id: str, data: Any) -> str:
        helper = CryptographyHelper()
        data = json.dumps(data)
        encrypted_data = helper.encrypt_data(data)
        self.keys[item_id] = helper.get_key()
        return encrypted_data

    def decrypt_item(self, item_id: str, encrypted_data: str, provided_key: str) -> dict | None:
        key = self.keys.get(item_id)
        if not key:
            raise ValueError("No key found for the given item ID.")
        if provided_key != key:
            raise ValueError("Provided key does not match the stored key.")
        helper = CryptographyHelper(key=provided_key.encode())
        try:
            data = helper.decrypt_data(encrypted_data)
            return json.loads(data)
        except InvalidToken:
            return None
