from datetime import datetime, timedelta

from draw import draw_menu, draw_books, draw_members, draw_overdue

def search_book(db,book):
    result = db.books.find()
    if book: result = db.books.find({'title': book})
    draw_books(result)
    input()

def borrow_book(db,member,book):
    return

def return_book(db,member,book):
    return

def view_member(db,member):
    result = db.members.find()
    if member: result = db.members.find({'email': member})
    draw_members(result)
    input()

def overdue_books(db):
    result = db.borrowings.find({'returned': {'$eq': None}, 'return_by' : {'$lt': datetime.now()}})
    draw_overdue(result)
    input()

def validate_borrow(db,member):
    #max 3 borrowed and none overdue
    result = db.borrowings.find({'member': member})

def library_menu(db):
    while True:
        draw_menu()

        match input('>>> '):
            case '1':
                search_book(db, 
                    input('Enter title, blank for all: ').lower().title())
            case '2':
                pass
            case '3':
                pass
            case '4':
                view_member(db, 
                    input('Enter email, blank for all: ').lower())
            case '5':
                overdue_books(db)
            case '6':
                quit()
            case '_':
                continue