from dataclasses import dataclass, field
from datetime import datetime
from typing import Tuple, List


@dataclass
class Medication:
    name: str
    amount: int


@dataclass
class Prescription:
    medications: tuple[Medication, ...]
    additional_info: str = "-"

    def to_dict(self):
        return {
            "medications": [{"name": med.name, "amount": med.amount} for med in self.medications],
            "additional_info": self.additional_info
        }


@dataclass
class MedicalRecord:
    id: str
    prescription: Prescription
    timestamp: datetime
    note: str = ""

    def __init__(self, patient_id, prescription: Prescription, note: str):
        self.id = patient_id
        self.prescription = prescription
        self.note = note
        self.timestamp = datetime.now()

    def to_dict(self):
        return {
            "id": self.id,
            "prescription": self.prescription.to_dict(),
            "timestamp": self.timestamp.isoformat(),
            "note": self.note
        }
