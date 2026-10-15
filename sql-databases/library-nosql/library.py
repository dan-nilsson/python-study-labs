from draw import draw_menu, draw_books

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
    return

def overdue_books(db):
    return

def validate_borrow(db,member):
    return True

def library_menu(db):
    while True:
        draw_menu()

        match input('>>> '):
            case '1':
                search_book(db, 
                    input('Enter Title, blank for all: ').lower().title())
            case '2':
                pass
            case '3':
                pass
            case '4':
                pass
            case '5':
                pass
            case '6':
                quit()
            case '_':
                continue