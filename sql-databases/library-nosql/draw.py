import os, time

menu_width = 50
menu_options = ['LIBRARY','1. search books 2. borrow book', '3. return book 4. member profiles', '5. overdue books 6. EXIT']
side = '#'

def draw_menu() -> None:
    draw_lines_aligned(menu_options,pad_over=2,pad_under=2)


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