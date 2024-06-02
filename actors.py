from dataclasses import dataclass
from smart_contract import SmartContract
from datetime import date
from enum import Enum


class Actor:
    def write_medical_record(smart_contract: SmartContract):
        pass

    def read_medical_record(smart_contract: SmartContract):
        pass

    def modify_medical_record(smart_contract: SmartContract):
        pass


class Gender(Enum):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"


@dataclass
class Contact:
    email: str = "-"
    phone: str = "-"


@dataclass
class Patient:
    id: str
    first_name: str
    last_name: str
    birthdate: date
    gender: Gender
    contact: Contact

    def __init__(
        self,
        first_name: str,
        last_name: str,
        birthdate: date,
        gender: Gender,
        contact: Contact,
    ):
        self.id = ""  # TODO: create standard of IDs creation
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = birthdate
        self.gender = gender
        self.contact = contact


@dataclass
class Doctor:
    id: str
    first_name: str
    last_name: str
    specialization: str
    contact: Contact

    def __init__(
        self, first_name: str, last_name: str, specialization: str, contact: Contact
    ):
        self.id = ""  # TODO: create standard of IDs creation
        self.first_name = first_name
        self.last_name = last_name
        self.specialization = specialization
        self.contact = contact


@dataclass
class EmergencyEntity:
    id: str
    name: str

    def __init__(self, name: str):
        self.id = ""  # TODO: create standard of IDs creation
        self.name = name
