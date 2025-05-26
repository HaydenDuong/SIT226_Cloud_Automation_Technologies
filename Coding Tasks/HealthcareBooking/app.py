import psycopg2
from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Database Configuration
DB_NAME = "healthcare"
DB_USER = "postgres"
DB_PASS = "qelol669"
# When running in Docker, DB_HOST should be the service name of the PostgreSQL container
DB_HOST = "postgres-db" 
DB_PORT = "5432"

def get_db_connection():
    conn = psycopg2.connect(
        dbname=DB_NAME, 
        user=DB_USER,
        password=DB_PASS,
        host=DB_HOST,
        port=DB_PORT
    )
    return conn

@app.route('/')
def home():
    return "Healthcare Appointment Booking System"

@app.route('/book')
def book():
    return render_template('book.html')

@app.route('/book-appointment', methods=['POST'])
def book_appointment():
    try:
        data = request.form
        patient_name = data['patient_name']
        doctor_id = data['doctor_id']
        appointment_time = data['appointment_time']

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO appointments (patient_name, doctor_id, appointment_time) VALUES (%s, %s, %s) RETURNING id",
            (patient_name, doctor_id, appointment_time)
        )
        appointment_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({"message": "Appointment booked successfully!", "appointment_id": appointment_id}), 201
    except Exception as e:
        print(f"Error in /book-appointment: {e}") 
        return jsonify({"error": str(e)}), 500

@app.route('/appointments', methods=['GET'])
def get_appointments():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, patient_name, doctor_id, TO_CHAR(appointment_time, 'YYYY-MM-DD HH24:MI:SS') as appointment_time FROM appointments ORDER BY appointment_time DESC")
        appointments = cur.fetchall()
        cur.close()
        conn.close()

        appointments_list = []
        for row in appointments:
            appointments_list.append({
                "id": row[0],
                "patient_name": row[1],
                "doctor_id": row[2],
                "appointment_time": row[3]
            })
        return jsonify(appointments_list), 200
    except Exception as e:
        print(f"Error in /appointments: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # When running with `flask run` (like in the Dockerfile CMD), 
    # host and port are typically set by FLASK_RUN_HOST and FLASK_RUN_PORT env vars.
    # The app.run() in __main__ is more for direct `python app.py` execution.
    # For Docker, the CMD ["flask", "run"] with ENV FLASK_RUN_HOST 0.0.0.0 takes care of it.
    app.run(host='0.0.0.0', port=5000) # This line is fine for direct execution too.