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

@app.route('/get_tk')
def get_tk():
    book_date_str = request.args.get('date')
    book_date = datetime.strptime(book_date_str, '%Y-%m-%d').date()
    get_tk = Ticket.query.filter_by(date=book_date).all()
    return jsonify([{'quantity': ticket.quantity} for ticket in get_tk])


if __name__ == '__main__':
    app.run(debug=True)
