from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\Bongeka.Mpofu\\DB Browser for SQLite\\tickets.db'
db = SQLAlchemy(app)

class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

# Create the database tables (Run this only once)
# db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/available_tickets')
def available_tickets():
    selected_date_str = request.args.get('date')
    selected_date = datetime.strptime(selected_date_str, '%Y-%m-%d').date()
    available_tickets = Ticket.query.filter_by(date=selected_date).all()
    return jsonify([{'date': ticket.date.strftime('%Y-%m-%d'), 'quantity': ticket.quantity} for ticket in available_tickets])

if __name__ == '__main__':
    app.run(debug=True)
