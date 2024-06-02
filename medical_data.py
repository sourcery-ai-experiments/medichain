from dataclasses import dataclass, field
from datetime import datetime
from typing import Tuple, List


@dataclass
class Medication:
    name: str
    amount: int


@dataclass
class Prescription:
    medications: Tuple[Medication]
    additional_info: str = "-"


@dataclass
class MedicalRecord:
    id: str
    prescription: Prescription
    timestamp: datetime
    note: str = ""

    def __init__(self, prescription: Prescription, note: str):
        self.id = ""  # TODO: create standard of IDs creation
        self.prescription = Prescription
        self.note = note
        self.timestamp = datetime.now()


@dataclass
class MedicalHistory:
    records: List[MedicalRecord] = field(default_factory=list)

    # TODO: Authorization system
    def read(self) -> str:
        print(self.records)

    def write(self, record: MedicalRecord) -> None:
        self.records.append(record)

    def edit(self):
        pass
