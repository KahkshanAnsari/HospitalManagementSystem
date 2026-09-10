# Hospital Management System - Version 1.0
# Features: Add and view patients

patients = []

def add_patient(patient_id, name, age, disease):
    patient = {
        "id": patient_id,
        "name": name,
        "age": age,
        "disease": disease
    }
    patients.append(patient)
    print("Patient", name, "added successfully")

def view_patients():
    print("Patient Records:")
    for patient in patients:
        print(
            "ID:", patient["id"],
            "Name:", patient["name"],
            "Age:", patient["age"],
            "Disease:", patient["disease"]
        )
