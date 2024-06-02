from key import Key
from actors import Patient, Doctor, Gender, Contact
from datetime import date
from smart_contract import SmartContract
from medical_data import MedicalHistory, MedicalRecord, Prescription, Medication


def main() -> None:
    dummy_data = {"patient_id": "1238912", "diagnosis": "sdadsdaasd"}
    key = Key(dummy_data)
    print(key.value)
    patient = Patient(
        first_name="Jan",
        last_name="Kowalski",
        birthdate=date(year=2000, month=2, day=19),
        gender=Gender.MALE,
        contact=Contact(email="j.kowalski@wupe.peel"),
    )
    doctor = Doctor(
        first_name="Marcin",
        last_name="Nowak",
        specialization="cardiology",
        contact=Contact(email="m.nowak@wupe.peel", phone="312645978"),
    )
    smart_contract = SmartContract(
        patient_id=patient.id,
        doctor_id=doctor.id,
        read=(patient.id, doctor.id),
        write=(doctor.id),
        edit=(),
    )
    # smart_contract.medical_history.write(
    #     MedicalRecord(Prescription(Medication(name="Paracetamol", amount=3)))
    # )

    def hello():
        print("siema")

    print(type(hello))


if __name__ == "__main__":
    main()
