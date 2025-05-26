from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return "Healthcare Appointment Booking System"

@app.route('/book')
def book():
    return render_template('book.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5000)