from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Healthcare Appointment Booking System"

@app.route('/book')
def book():
    return "Book an Appointment"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5000)