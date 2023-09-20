from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

#Model - python - y version of a db table. Through classes
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(100), unique=True, nullable=False)
    author = db.Column(db.String(45), nullable=False)
    publisher = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return f"{self.book_name} - {self.author}, published by {self.publisher}"


#route says when you go to this url... perform this following function
@app.route('/')
def index():
    return 'Hello!'

#create a route that when visited, displays all the books in the database
@app.route('/books')
def get_books():
    books = Book.query.all()
    output = []

    for book in books:
        book_data = {'book_name': book.book_name , 'author': book.author, 'publisher': book.publisher}
        output.append(book_data)
    return {"books": output}