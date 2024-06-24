import json
from dataclasses import dataclass
from datetime import datetime

from audit_trail import AuditTrail
from blockchain import Blockchain
from encryption import CryptographyManager, CryptographyHelper
from medical_data import MedicalHistory, MedicalRecord, Medication, Prescription


@dataclass
class AccessControl:
    read: tuple[str, ...]
    write: tuple[str, ...]
    edit: tuple[str, ...]

    def can_read(self, accessing_entity_id) -> bool:
        return accessing_entity_id in self.read

    def can_write(self, accessing_entity_id) -> bool:
        return accessing_entity_id in self.write

    def can_edit(self, accessing_entity_id) -> bool:
        return accessing_entity_id in self.edit


@dataclass
class SmartContract:
    patient_id: str
    doctor_id: str
    access_control: AccessControl
    medical_history: MedicalHistory
    blockchain: Blockchain

    def __init__(
            self,
            patient_id: str,
            doctor_id: str,
            read: tuple[str, ...],
            write: tuple[str, ...],
            edit: tuple[str, ...],
            blockchain: Blockchain,
            crypto_manager: CryptographyManager,
    ):
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.access_control = AccessControl(read=read, write=write, edit=edit)
        self.medical_history = MedicalHistory()
        self.blockchain = blockchain
        self.encryption = crypto_manager

    def handle_access(self, access_type: str):
        match access_type:
            case "read":
                pass
            case "write":
                pass
            case "edit":
                pass
            case _:
                print("Something went wrong.")

    def execute(self, func: callable):
        func()

    def add_medical_record(self, patient_id: str, comment: str, predicaments: list[tuple[str, int]]):

        if self.access_control.can_write(self.doctor_id):
            # Create MedicalRecord
            medications = [Medication(name=p[0], amount=p[1]) for p in predicaments]
            prescription = Prescription(medications=tuple(medications))
            medical_record = MedicalRecord(prescription=prescription, note=comment, patient_id=patient_id)

            # Encrypt data
            medical_record = medical_record.to_dict()
            encrypted_data = self.encryption.encrypt_item(item_id=patient_id, data=medical_record)
            audit_trail = AuditTrail(patient_id=patient_id, doctor_id=self.doctor_id)

            # Create transaction and mine block
            transaction = {
                "medical_data": encrypted_data,
                "audit_trail": audit_trail.to_dict(),
            }

            # Add the transaction to the blockchain
            self.blockchain.add_transaction(transaction)

            mined = False

            if len(self.blockchain.pending_transactions) >= 1:
                mined = self.blockchain.mine_pending_transactions()

            encryption_key = self.encryption.keys[patient_id]

            return mined, encryption_key

        else:
            raise PermissionError("Doctor does not have write access to add medical records.")

    def view_medical_record(self, patient_id: str, decryption_key: str) -> dict:

        transaction = None

        for block in self.blockchain.chain:
            for tx in block.transactions:
                tx_medical = self._decrypt(tx['medical_data'], decryption_key)
                if tx_medical is not None:
                    if tx_medical.get('id') == patient_id:
                        transaction = tx
                        medical_data = self._decrypt(transaction['medical_data'], decryption_key)
                        medical_data['timestamp'] = datetime.fromisoformat(medical_data['timestamp'])
                        return medical_data

        if not transaction:
            raise ValueError("No medical record found with the given ID.")

    def _decrypt(self, encrypted_data: str, key: str) -> dict:
        return self.encryption.decrypt_item(item_id=self.patient_id, encrypted_data=encrypted_data,
                                            provided_key=key)
