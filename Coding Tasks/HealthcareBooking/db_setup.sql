CREATE DATABASE healthcare;

\c healthcare

CREATE TABLE appointments (
    id SERIAL PRIMARY KEY,
    patient_name VARCHAR(100),
    doctor_id INT,
    appointment_time TIMESTAMP,
);