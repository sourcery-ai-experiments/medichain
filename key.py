from dataclasses import dataclass
from typing import Any
import hashlib


@dataclass
class Key:
    value: str

    def __init__(self, unserialized_data: Any):
        self.value = self.encrypt_data(unserialized_data)

    def encrypt_data(self, data: Any) -> str:
        serialized_data = str(data)
        encrypted_data = hashlib.sha256(serialized_data.encode()).hexdigest()
        return encrypted_data
