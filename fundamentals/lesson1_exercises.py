'''
Lab1 - Lesson 1 - 260908
'''

from datetime import datetime

#Part A - 1
data = ['Daniel Nilsson','Lexicon - Python & AI','Python Fundamentals - Lesson 1']
#print(*data, sep='\n')

#Part A - 2
name = 'Daniel Nilsson'
age = 41
height = 1.85
is_student = True
'''
print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))

#Part A - 3
is_student = 1
print(is_student, type(is_student))
# variables are not type sensitive nor static. they change type on assignement and can be reassigned.
'''

#Part A - 4
a = 15
b = 10
'''
print('a + b = '+str(a+b))
print('a - b = '+str(a-b))
print('a multiplied with b = '+str(a*b))
print('a divided by b = '+str(a/b))
print('floor division of a over b = '+str(a//b))
print('the remainder of a over b = '+str(a%b))
print('a to the power of b = '+str(a**b))
'''
#Part A - 5
#string to int - to be used in calculations
#int to float - a non integer value would be rounded
#number to string - to be able to concatinate with string

#Part B - 1
def profile_program():
    print('Please enter your name:')
    input_name = input()
    print('Please enter your year of birth:')
    input_year = int(input())
    current_year = datetime.now().year
    print(f'{input_name} is approx {current_year-input_year} years old.')

#profile_program()

#Part B - 2

def discount_price():
    print('What is the price of the item?:')
    price = float(input())
    print('What is the discount percentage?:')
    discount = float(input())
    final_price = price * (1 - (discount/100))
    print(f'The discounted price if the item is {round(final_price,2)}!')

#discount_price()

#Part B - 3
def c_to_f():
    print('What is the temperature in Celsius?:')
    temp_c = int(input())
    temp_f = temp_c * 9/5 + 32
    print(f'{temp_c} degrees Celsius equals {temp_f} degrees in Freedom-Units!')

#c_to_f()

#Part B - 4
def calc_room_metrics():
    print('Please enter the length of the room in meters:')
    length = float(input())
    print('Please enter the width of the room in meters:')
    width = float(input())
    area = length * width
    perimiter = length * 2 + width * 2
    print(f'The area of the room is {area}m2 and the perimiter of the room is {perimiter}m long.')

#calc_room_metrics()

#Part B - 5
#Will get typeerror or valueerror if trying to cast/convert

#Part C - 1
def string_variations():
    sentence = '  Hello everybody! Python is very powerful and nice.  '
    print(f'Length is {len(sentence)}')
    print(sentence.upper())
    print(sentence.lower())
    print(sentence.strip())

#string_variations()

#Part C - 2
def formated_name():
    print('Enter your first name')
    first = input()
    print('Enter your last name')
    last = input()
    print(f'Your name is {first} {last}!')

#formated_name()

#Part C - 3
def python_string():
    pyth = 'python programming'
    print(  f'First char: {pyth[0]}\n'
            f'Last char: {pyth[-1]}\n'
            f'First 6 chars: {pyth[:6]}\n'
            f'Last 11 chars: {pyth[-11:]}\n'
            f'Reversed: {pyth[::-1]}'
        )

#python_string()

#Part C - 4
def username_generator():
    print('Enter first name:')
    first = input().lower().strip()
    print('Enter last name:')
    last = input().lower().strip()
    user_name = first[:3] + last[:5]
    print(f'Your username is {user_name} .')

#username_generator()

#Part C - 5
def email_parser():
    email = 'daniel@nilsson.se'
    parts = email.split('@')
    print(f'Username: {parts[0]} Domain: {parts[1]}')

#email_parser()

#Part C - 6
def switch_lang():
    sentence = 'Java is a powerful programming language!'
    upgrade = sentence.replace('Java','Python')
    print(upgrade)

#switch_lang()

#Part D - 1
'''
a[0] first character
a[1] second character
a[-1] last character
a[1:] everything but the first char
a[:-1] everything but the last char
a[::2] every other char
a[::-1] reversed
a[:5] the first 5 chars
'''

#Part D - 2
def ai_slice():
    ai = 'Artificial Intelligence'
    print(  f'{ai.split(' ')[0]}\n'     #Artificial
            f'{ai.split(' ')[1]}\n'     #Intelligence
            f'{ai[:]}\n'                #whole string
            f'{ai[::-1]}\n'             #reverse of string
            f'{ai[::2]}\n'              #Atfca nelge
            f'{ai[11:]}'                #Intelligence
        )

#ai_slice()

#Part D - 3
def split_strip_replace():
    s = 'Python is a powerful programming language.  '
    print(  f'{s.split(' ')[0]}\n'              #makes a list of the words. can pick out by index
            f'{s.strip()}\n'                    #removes leading / trailing white spaces
            f'{s.replace('powerful','useful')}' #replaces matched string
        )

#split_strip_replace()

#Part D - 4
def string_immutability():
    s = 'immutable'
    #s[0] = ' '     #TypeError: 'str' object does not support item assignment
    s = s[2:]
    print(s)        

#string_immutability()

#Part E - 1-6
def get_to_know_you():
    print('What\'s your first name?:')
    first = input().strip()
    print('What\'s your last name?:')
    last = input().strip()
    print('What city are you from?:')
    city = input().strip()
    print('What year where you born?:')
    birth = input().strip()
    print('What\'s your favourite programming language?:')
    prog = input().strip()
    user_id = first.lower()[:3]+last.lower()[:3]+birth[-2:]
    initials = first.upper()[0]+last.upper()[0]
    print(  f'Hello sir/mam {initials}, {first} {last}, userid: {user_id}. Where you born in {city} year {birth} or have you maybe moved since. '
            f'I also like {prog} it\'s one of my favourites as well.'
        )
    print(f'{initials} {len((first+last))} {prog[::-1]}')

#get_to_know_you()

#Part F - 1
def seconds_converter(sec):
    hours = sec // 3600
    minutes = sec % 3600 // 60
    seconds = sec % 3600 % 60
    print(f'Hours: {hours} Minutes: {minutes} Seconds: {seconds}')

#seconds_converter(int(input('Enter seconds to convert to H:M:S :')))

#Part F - 2
def print_digits(four_int):
    dig_4 = four_int % 10
    dig_3 = four_int % 100
    dig_2 = four_int % 1000
    dig_1 = (four_int % 10000 - dig_2) / 1000
    dig_2 = (dig_2 - dig_3) / 100
    dig_3 = (dig_3 - dig_4) / 10
    
    print(  f'digit 1: {int(dig_1)} '
            f'digit 2: {int(dig_2)} '
            f'digit 3: {int(dig_3)} '
            f'digit 4: {int(dig_4)} '
        )

#print_digits(int(input('Enter a 4 digit integer:')))

#Part F - 3
def text_mask(text):
    masked = text[:2] + '*' * (len(text)-4) + text[-2:]
    print(f'Masked word: {masked}')

#text_mask(input('Enter a word:'))

#Part F - 4
def predict_output():
    num = 10
    print(f'num is Type: {type(num)}')
    num = num / 3
    print(f'num is Type: {type(num)}')
    num = str(num)
    print(f'num is Type: {type(num)}')
    num = num[:1]
    print(f'num is {num}')
    num = num * 3
    print(f'num is {num}')

#predict_output()