from datetime import datetime, timedelta

from dbtools import sanitize_match
from draw import   (draw_menu, draw_books, draw_members, draw_overdue, draw_borrow, draw_return,
                    draw_error, draw_report_menu, draw_most_borrowed, draw_average_rating)

def search_book(db,book):
    result = db.books.find()
    if book: result = db.books.find({'title': sanitize_match(book)})
    draw_books(result)

def borrow_book(db,member,book):
    clean_member, clean_book = int(sanitize_match(member)), int(sanitize_match(book))
    num_borrowed, num_overdue, num_available = validate_borrow(db, clean_member, clean_book)
    if num_borrowed < 3 and not num_overdue and num_available:
        result = db.borrowings.insert_one({
            'member': clean_member, 'book': clean_book,
            'borrowed': datetime.now(), 'return_by': datetime.now() + timedelta(days=14), 'returned': None})
        db.books.update_one({'_id': clean_book},{'$inc': {'available': -1}})
    draw_borrow(name_from_id(db,clean_member,'members'),name_from_id(db,clean_book,'books'),
                num_borrowed,num_overdue,num_available)

def return_book(db,member,book):
    clean_member, clean_book = int(sanitize_match(member)), int(sanitize_match(book))
    borrow_found, is_overdue = validate_return(db,clean_member, clean_book)
    if not borrow_found: 
        draw_return(name_from_id(db,clean_member,'members'),name_from_id(db,clean_book,'books'),
                    is_overdue,not_found=True)
    else:
        result = db.borrowings.update_one(  {'member': clean_member, 'book': clean_book},
                                            {'$set': {'returned': datetime.now()}})
        db.books.update_one({'_id': clean_book},{'$inc': {'available': 1}})
        draw_return(name_from_id(db,clean_member,'members'),name_from_id(db,clean_book,'books'),is_overdue)

def view_member(db,member):
    result = db.members.find()
    if member: result = db.members.find({'email': sanitize_match(member)})
    draw_members(result)

def overdue_books(db,member):
    clean_member = sanitize_match(member)
    result = db.borrowings.find({'returned': None, 'return_by' : {'$lt': datetime.now()}})
    if clean_member: result = db.borrowings.find({  'member': int(clean_member), 'returned': None, 
                                                    'return_by' : {'$lt': datetime.now()}})
    draw_overdue(result)

def validate_borrow(db,member,book) -> tuple:
    ''' (member # borrows, member # overdue, book # available) '''
    num_borrowed = db.borrowings.count_documents({'member': member, 'returned': None})
    num_overdue = db.borrowings.count_documents({   'member': member, 'returned': None,
                                                    'return_by': {'$lt': datetime.now()}})
    num_available = db.books.count_documents({'_id': book, 'available': {'$gt': 0}})
    return (num_borrowed,num_overdue,num_available)

def validate_return(db,member,book) -> tuple:
    ''' (borrow is found, is borrow overdue)'''
    return (db.borrowings.count_documents({'member': member, 'book': book, 'returned': None}),
            db.borrowings.count_documents({ 'member': member, 'book': book, 'returned': None,
                                            'return_by': {'$lt': datetime.now()}}))

def name_from_id(db,id,col) -> str:
    match col:
        case 'members': return (f'{db.members.find_one({'_id': id}).get('first_name')} '+
                                f'{db.members.find_one({'_id': id}).get('last_name')}')
        case 'books': return db.books.find_one({'_id': id}).get('title')

def library_menu(db):
    while True:
        draw_menu()

        match input('>>> '):
            case '1':
                search_book(db, 
                    input('Enter title, blank for all: ').lower().title())
            case '2':
                member_id = input('MemberID: ')
                book_id = input('BookID: ')
                if member_id.isdigit() and book_id.isdigit():
                    borrow_book(db, member_id, book_id)
                else: draw_error('INVALID INPUT')
            case '3':
                member_id = input('MemberID: ')
                book_id = input('BookID: ')
                if member_id.isdigit() and book_id.isdigit():
                    return_book(db, member_id, book_id)
                else: draw_error('INVALID INPUT')
            case '4':
                view_member(db, 
                    input('Enter email, blank for all: ').lower().strip())
            case '5':
                member_id = input('MemberID, blank for all: ')
                if member_id.isdigit() or member_id == '':
                    overdue_books(db,member_id)
                else: draw_error('INVALID INPUT')
            case '6':
                quit()
            case '0':
                report_menu(db)
            case '_':
                continue

'''
MongoDB Aggregate Pipeline Reports
'''

def report_menu(db) -> None:
    while True:
        draw_report_menu()

        match(input('>>> ')):
            case '1':
                most_borrowed(db)
            case '2':
                average_rating(db)
            case '3':
                return
            case '_':
                continue

def most_borrowed(db) -> None:
    pipe = [{'$group' : {'_id': '$book', 'count': {'$sum': 1} }},
            {'$sort': {'count': -1}}, {'$limit': 3}]
    result = db.borrowings.aggregate(pipe)
    top3 = [(name_from_id(db,int(doc.get('_id')),'books'), doc.get('count')) for doc in result]
    draw_most_borrowed(top3)

def average_rating(db) -> None:
    pipe = [{'$group': {'_id': '$book', 'avg': {'$avg': {'$sum': '$rating'}}}},
            {'$sort': {'avg': -1}}]
    result = db.reviews.aggregate(pipe)
    ratings = [(name_from_id(db,int(doc.get('_id')),'books'), doc.get('avg')) for doc in result]
    draw_average_rating(ratings)