import sqlite3, random, datetime
from models import Book


def getNewId():
    return random.getrandbits(28)

    'id': self.id
    'book_name': self.title
    'author': self.author
    'publisher':self.publisher


books = [
    # {
    #    'id': '9780316044691'
    #    'book_name': 'Lone Survivor'
    #    'author': 'Marcus Luttrell'
         'publisher': Little, Brown and Company
    # },
    {
        'id': '9781416511946',
        'book_name': 'The Heroin Diaries: A Year in the Life of a Shattered Rock Star',
        'author': 'Nikki Sixx and Ian gittins'
        'publisher': 'MTV Books'
    },
    
    {
        'id': '306842',
        'book_name': "Harry Potter and the Sorcerer's Stone",
        'author': 'J.K Rowling'
        'publisher': 'Bloomsbury (UK)'
    },

    
    {
        'id': '9780747545118',
        'book_name': 'Harry Potter and the Prisoner of Azkaban',
        'author': 'J.K Rowling'
        'publisher': 'Bloomsbury (UK)'
    },
]    

def connect():
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, available BOOLEAN, title TEXT, timestamp TEXT)")
    conn.commit()
    conn.close()
    for i in books:
        bk = Book(getNewId(), i['available'], i['title'], i['timestamp'])
        insert(bk)

def insert(book):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO books VALUES (?,?,?,?)", (
        self.id,
        self.book_name,
        self.author,
        self.publisher
    ))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM books")
    rows = cur.fetchall()
    books = []
    for i in rows:
        book = Book(i[0], True if i[1] == 1 else False, i[2], i[3])
        books.append(book)
    conn.close()
    return books

def update(book):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("UPDATE books SET available=?, title=? WHERE id=?", (book.available, book.title, book.id))
    conn.commit()
    conn.close()

def delete(theId):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM books WHERE id=?", (theId,))
    conn.commit()
    conn.close()

def deleteAll():
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM books")
    conn.commit()
    conn.close()