from dataclasses import dataclass
from datetime import datetime


@dataclass
class AuditTrail:
    id: str
    timestamp: datetime
    patient_id: str
    doctor_id: str
    # AccessType possibly?

    def __init__(self, patient_id: str, doctor_id: str):
        self.id = ""  # TODO: create standard of IDs creation
        self.timestamp = datetime.now()
        print(self.timestamp)
        self.patient_id = patient_id
        self.doctor_id = doctor_id
