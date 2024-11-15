from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
import os

# Initialize the Flask app
app = Flask(__name__)

# Configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school.db'  # SQLite Database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')  # Use environment variables for security
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')  # Use environment variables for security

# Initialize extensions
db = SQLAlchemy(app)
mail = Mail(app)

# Models for Database
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    experience = db.Column(db.Integer, nullable=False)
    qualifications = db.Column(db.Text, nullable=False)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(50), nullable=False)  # New or Former

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/employee', methods=['GET', 'POST'])
def employee():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        subject = request.form['subject']
        experience = request.form['experience']
        qualifications = request.form['qualifications']

        # Create a new Employee record in the database
        new_employee = Employee(name=name, email=email, phone=phone, subject=subject,
                                experience=experience, qualifications=qualifications)

        try:
            db.session.add(new_employee)
            db.session.commit()

            # Send Confirmation Email
            send_email(email, "Application Received", "Thank you for applying as a teacher at Bashwam School!")

            return redirect(url_for('employee'))  # Redirect to the same page or a success page
        except Exception as e:
            db.session.rollback()
            print(e)
            return "There was an issue with your registration."

    return render_template('employee.html')


@app.route('/student_registration', methods=['GET', 'POST'])
def student_registration():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        status = request.form['status']  # New or Former Student

        # Create a new Student record
        new_student = Student(name=name, email=email, phone=phone, status=status)

        try:
            db.session.add(new_student)
            db.session.commit()

            # Send Confirmation Email
            send_email(email, "Registration Received", "Thank you for registering at Bashwam School!")

            return redirect(url_for('student_registration'))  # Redirect to the same page or a success page
        except Exception as e:
            db.session.rollback()
            print(e)
            return "There was an issue with your registration."

    return render_template('register.html')


def send_email(to_email, subject, body):
    try:
        msg = Message(subject, sender=app.config['MAIL_USERNAME'], recipients=[to_email])
        msg.body = body
        mail.send(msg)
    except Exception as e:
        print(f"Error sending email: {e}")


if __name__ == '__main__':
    app.run(debug=True)
