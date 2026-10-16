import os, time, datetime

menu_width = 100
menu_options = ['LIBRARY MAIN MENU','1. search books 2. borrow book', '3. return book 4. member profiles', 
                '5. overdue books 0. report menu 6. QUIT']
report_options = ['REPORT MENU','1. most borrowed 2. average ratings','3. BACK']
side = '#'

def draw_menu() -> None:
    draw_lines_aligned(menu_options,pad_over=2,pad_under=2)

def draw_books(books) -> None:
    lines =[f'ID: {doc.get('_id')} Title: {doc.get('title')} Author: {doc.get('author')} ' 
            f'Year: {doc.get('year')} Genres: {doc.get('genres')} available: {doc.get('available')}' 
            for doc in books]
    draw_lines(lines,halt=True)

def draw_members(members) -> None:
    lines =[f'ID: {doc.get('_id'):<3} Name: {f'{doc.get('first_name')} {doc.get('last_name')}':<15} '
            f'Email: {doc.get('email'):<25} City: {doc.get('city') if not doc.get('city') else f'{doc.get('city'):<10}'} '
            f'Joined: {doc.get('joined').date()}'
            for doc in members]
    draw_lines(lines,halt=True)

def draw_overdue(overdue) -> None:
    lines = [f'MemberID: {doc.get('member')} BookID: {doc.get('book')} Return by: {doc.get('return_by').date()}' for doc in overdue]
    draw_lines(lines,halt=True)

def draw_borrow(member,book,borrowed=0,overdue=0,available=0) -> None:
    lines =[f'Member: {member} has borrowed Book: {book}. Borrowed: {borrowed+1}' if not overdue and borrowed < 3 and available else
            f'You are not allowed to borrow more books. Borrowed: {borrowed} Overdue: {overdue}' if available else
            f'No more available copies of Book {book}']
    draw_lines(lines,halt=True)

def draw_return(member,book,is_overdue,not_found=False):
    lines =[f'Book: {book} returned by Member: {member}. Thank you!' if not not_found else
            f'LOAN NOT FOUND IN DATABASE']
    draw_lines(lines,halt=True)

def draw_report_menu() -> None:
    draw_lines_aligned(report_options,pad_over=2,pad_under=2)

def draw_most_borrowed(top3) -> None:
    lines =([f'MOST BORROWED BOOKS']+
            [f'{i}. {book_name:<25} : borrowed {count} times.' for i,(book_name,count) in enumerate(top3,1)])
    draw_lines(lines,halt=True)

def draw_average_rating(ratings) -> None:
    lines =([f'BOOKS AVERAGE RATINGS']+
            [f'{i}. {book_name:<25} -  {rating}/10' for i,(book_name,rating) in enumerate(ratings,1)])
    draw_lines(lines,halt=True)

def draw_lines(lines,halt=False):
    if lines:
        pad = 4 if len(lines) == 1 else 0
        draw_lines_aligned(lines,align='left',pad_side=2,width=120,pad_over=pad,pad_under=pad)
    else: draw_error('NO RESULTS FOUND')
    if halt: input()

def draw_error(line) -> None:
    draw_lines_aligned([line],pad_over=4,pad_under=4)

'''
Generalized drawing methods with borders
'''
def draw_lines_aligned( lines,width=menu_width,align='center',
                        pad_side=0,pad_over=0,pad_under=0,pause=0,clear=True) -> None:
    if clear: screen_clear()
    draw_sep(width,empty_under=pad_over)
    if align == 'center': print(*[draw_line_center(l,width) for l in lines],sep='\n')
    if align == 'left': print(*[draw_line_left((' '*pad_side)+l,width) for l in lines],sep='\n')
    draw_sep(width,empty_over=pad_under)
    time.sleep(pause)

def draw_line_center(line='',width=menu_width) -> str:
    return side+('{:^'+str(width-2)+'s}').format(line)+side

def draw_line_left(line='',width=menu_width) -> str:
    return side+('{:<'+str(width-2)+'s}').format(line)+side

def draw_sep(width=menu_width,empty_over=0,empty_under=0) -> None:
    if empty_over: print(*[draw_line_center(width=width)]*empty_over,sep='\n')
    print(f'##{'-'*(width-4)}##')
    if empty_under: print(*[draw_line_center(width=width)]*empty_under,sep='\n')

def screen_clear() -> None:
    if os.name == 'nt': os.system('cls')
    else: os.system('clear')