from datetime import datetime, timedelta

from dbtools import sanitize_input

from draw import draw_menu, draw_books, draw_members, draw_overdue, draw_borrow

def search_book(db,book):
    result = db.books.find()
    if book: result = db.books.find({'title': {'$in': sanitize_input(book)}})
    draw_books(result)

def borrow_book(db,member,book):
    num_borrowed,num_overdue = validate_borrow(db,member)
    if num_borrowed < 3 and not num_overdue:
        result = db.borrowings.insert_one({
            'member': member, 'book': book,
            'borrowed': datetime.now(), 'return_by': datetime.now() + timedelta(days=14), 'returned': None})
    draw_borrow(member,book,num_borrowed,num_overdue)

def return_book(db,member,book):
    result = db.borrowings.update_one(
        {'member': {'$in': sanitize_input(member)}, 'book': {'$in': sanitize_input(book)}},
        {'returned': datetime.now()})

def view_member(db,member):
    result = db.members.find()
    if member: result = db.members.find({'email': {'$in': sanitize_input(member)}})
    draw_members(result)

def overdue_books(db):
    result = db.borrowings.find({'returned': {'$eq': None}, 'return_by' : {'$lt': datetime.now()}})
    draw_overdue(result)

def validate_borrow(db,member) -> tuple:
    #max 3 borrowed and none overdue
    num_borrowed = db.borrowings.count_documents({'member': {'$in': sanitize_input(member)}, 'returned': None})
    num_overdue = db.borrowings.count_documents({'member': {'$in': sanitize_input(member)}, 'returned': None,
        'return_by': {'$lt': datetime.now()}})
    return (num_borrowed,num_overdue)

def library_menu(db):
    while True:
        draw_menu()

        match input('>>> '):
            case '1':
                search_book(db, 
                    input('Enter title, blank for all: ').lower().title())
            case '2':
                borrow_book(db,
                    int(input('MemberID: ')),
                    int(input('BookID: ')))
            case '3':
                return_book(db,
                    input('MemberID: '),
                    input('BookID: '))
            case '4':
                view_member(db, 
                    input('Enter email, blank for all: ').lower().strip())
            case '5':
                overdue_books(db)
            case '6':
                quit()
            case '_':
                continue