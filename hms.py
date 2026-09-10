# Hospital Management System - Version 2.0
# Features: Patient management, appointments, doctors and billing

patients = []
appointments = []
doctors = []

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

def book_appointment(patient_id, doctor_name, date):
    appointment = {
        "patient_id": patient_id,
        "doctor": doctor_name,
        "date": date
    }
    appointments.append(appointment)
    print("Appointment booked with", doctor_name, "on", date)

def view_appointments():
    print("Appointments:")
    for appointment in appointments:
        print(
            "Patient ID:", appointment["patient_id"],
            "Doctor:", appointment["doctor"],
            "Date:", appointment["date"]
        )

def add_doctor(doctor_id, name, specialization):
    doctor = {
        "id": doctor_id,
        "name": name,
        "specialization": specialization
    }
    doctors.append(doctor)
    print("Doctor", name, "added successfully")

def view_doctors():
    print("Doctor Records:")
    for doctor in doctors:
        print(
            "ID:", doctor["id"],
            "Name:", doctor["name"],
            "Specialization:", doctor["specialization"]
        )

def calculate_bill(consultation_fee, medicine_cost, room_charges):
    total = consultation_fee + medicine_cost + room_charges
    print("Total Bill = Rs.", total)
    return total
