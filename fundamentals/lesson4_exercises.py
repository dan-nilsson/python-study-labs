'''
Lab4 - 260914
'''

#Part A - 1
def greet():
    print('Hello')

def show_course_name():
    print('Python Developer AI & ML')

def print_separator():
    print('-'*10)

# greet()
# print_separator()
# show_course_name()

#Part A - 2
def greet_person(name):
    print(f'Hello, {name}.')

def introduce(name,city):
    print(f'This is {name} from {city}.')

# greet_person('Göran')
# introduce('Hans','Skövde')

#Part A - 3
def add(a: int,b: int) -> int:
    return a + b

def subtract(a: int,b: int) -> int:
    return a - b

def multiply(a: int,b: int) -> int:
    return a * b

def divide(a: int,b: int) -> (int,float):
    return a / b

#Part A - 4
# def add(a,b):     Here a and b are parameters of the function add()
add(5, 3)          #Here we pass in 5 and 3 as arguments during a function call of add()

#Part A - 5
def calculate_area(w,h):
    return w * h

def total_area(rooms):
    total = 0
    for r in rooms:
        total += calculate_area(*r)
    return total

appartment = [(4,6),(4,4),(5,4),(2,3),(4,4)]
# print(total_area(appartment))

#Part B - 1
def is_even(number):
    return number % 2 == 0

# print(is_even(6))

#Part B - 2
def get_larger(a: int,b:int) -> int:
    if a >= b: return a
    else: return b

# print(get_larger(8,4))

#Part B - 3
def classify_score(score):
    if score >= 60: return 'PASS'
    return 'FAIL'

# print(classify_score(67))

#Part B - 4
def full_name(first_name,last_name):
    return f'{first_name} {last_name}'

# print(full_name('Daniel','Nilsson'))

#Part B - 5
def calculate_discount(price,percent):
    return price - price * (percent / 100)

# print(calculate_discount(500,25))

#Part B - 6
#If you print inside the function it can not be usefully used in other calculations


#Part C - 1
def greeting(name,greeting='Hello'):
    print(f'{greeting}, {name}')

# greeting('Ylva')
# greeting('Francis','Howdy')

#Part C - 2
def calculate_price(price,quantity=1,discount=0):
    return calculate_discount(price*quantity,discount)

# print(calculate_price(255))
# print(calculate_price(500,2,10))

#Part C - 3
def create_profile(name,city='Unknown',active=True):
    return dict({'name' : name, 'city' : city, 'active': active})

# print(create_profile('Therese'))
# print(create_profile('Urban','Umeå',False))

#Part C - 4
# print(create_profile(city='Malmö',active=True,name='Viktoria'))

#Part C - 5
# def invalid_order(default=True,parameter): 
# parameters with default values have to be after those without in order to be able to use function using defaults


#Part D - 1
num = [2,3,4,6,7,8,10,1]
def calculate_total(numbers):
    total = 0
    for n in numbers:
        total += n
    return total

# print(calculate_total(num))

#Part D - 2
def count_even(numbers):
    count = 0
    for n in numbers:
        if n % 2 == 0: count += 1
    return count

# print(count_even(num))

#Part D - 3
def get_long_words(words,min_length):
    long_words = []
    for w in words:
        if len(w) >= min_length: long_words.append(w)
    return long_words

# print(get_long_words(['Hello','Hello World','Python Rocks'],6))

#Part D - 4
students = [{'name' : 'Greta', 'score' : 90, 'grade' : 'A', 'active' : True},
            {'name' : 'Hansel', 'score' : 70, 'grade' : 'B', 'active' : True},
            {'name' : 'Bob', 'score' : 86, 'grade' : 'A', 'active' : True},
            {'name' : 'Frank', 'score' : 62, 'grade' : 'C', 'active' : False}
        ]
def find_student(students,name):
    for s in students:
        if s['name'] == name: return s
    return None

# print(find_student(students,'Bob'))

#Part D - 5
def average_score(students):
    return sum(s['score'] for s in students) / len(students)

# print(average_score(students))

#Part D - 6
def get_active_users(users):
    return [s for s in users if s['active']]

# print(*get_active_users(students), sep='\n')


#Part E - 1
def weather_report(temp):   
    print(f'The weather today is {hows_the_weather(temp)}.')

def hows_the_weather(temp):
    if temp >= 35: return 'hot'
    elif temp > 20: return 'warm'
    else: return 'cold'

def convert_temp(temp: int,to_cel=True) -> (int,float):
    if to_cel: return (temp - 32) / 1.8
    else: return (temp * 9 / 5) + 32

# weather_report(convert_temp(55))
# weather_report(convert_temp(77))
# weather_report(convert_temp(105))

#Part E - 2

items = [120,500,360,75]

def subtotal(price,dis):
    return discount(price,dis)

def discount(price,discount):
    return (price - (price * (discount / 100)))

def final_total(items, discount=0):
    return sum(subtotal(item,discount) for item in items)

# print(final_total(items))

#Part E - 3
# weather_report() refactored into hows_the_weather()

#Part E - 4
# Done - I do not apporove
'''
Part F
1. Create functions to normalize a participant name, validate an age range using boolean return values, calculate a registration fee based on age/student status, and create a participant dictionary. 
2. Create at least eight participant dictionaries using your functions. 
3. Write a function that receives the participant list and returns the total expected registration revenue. 
4. Write a function that returns only student participants. 
5. Write a function that returns the oldest participant. 
6. Write a function that creates a readable summary string for one participant. 
7. Keep input/output responsibilities separate from calculation functions as much as possible.
'''
#Part F - 1
participants = []

def register_participant(name: str,age: int,student:bool=True) -> dict:
    participants.append({'name' : name, 'age' : age, 'student' : student, 'reg_fee': calc_fee(age,student)})

def calc_fee(age,student=True):
    return 100 if age < 18 or age >= 18 and student else 200

# print(calc_fee(18, False))

#Part F - 2
register_participant('Mona',18)
register_participant('Hans',25)
register_participant('Lina',17,False)
register_participant('Göran',25,False)
register_participant('Bob',35)
register_participant('Frank',45,False)
register_participant('Johan',12)
register_participant('Börje',37)

# print(*participants,sep='\n')

#Part F - 3
def calc_registration_revenue(participants):
    return sum(p['reg_fee'] for p in participants)

# print(calc_registration_revenue(participants))

#Part F - 4
def student_list(participants):
    return [p for p in participants if p['student']]

# print(*student_list(participants),sep='\n')

#Part F - 5
def oldest_dude(participants):
    oldest = participants[0]
    for p in participants:
        if p['age'] > oldest['age']: oldest = p
    return oldest

# print(oldest_dude(participants))

#Part F - 6
def participant_print(p):
    print(  f'Name: {p['name']} Age: {p['age']} Student: {'Yes' if p['student'] else 'No'} '
            f'Registration Fee: {p['reg_fee']}.'
        )

# participant_print(oldest_dude(participants))

#Part G - 1
def min_and_max(num: [int]) -> tuple:
    '''Pretty neat'''
    min,max = num[0],0
    for n in num:
        if n < min: min = n
        if n > max: max = n
    return min,max

# print(min_and_max(num))

#Part G - 2
def palindrome(word: str) -> bool:
    '''Around and around we go'''
    return word.lower() == ''.join(reversed(word)).lower()

# print(palindrome('Hello'),palindrome('Anna'))

#Part G - 3
def count_character_freq(word: str) -> dict:
    '''A clear favourite'''
    out = {}
    for c in word:
        if c in out: out.update({c : out[c]+1}) 
        else: out.update({c : 1})
    return out

# print(count_character_freq('Himmalaya Mountain Range'))

#Part G - 4
numbahs = [-1,-5,2,8,10,0,0,-7,-7,7]
def pos_neg_zero(numbers : list) -> dict:
    '''This function is pretty groovy'''
    out = {'pos' : 0, 'neg' : 0, 'zero' : 0}
    for n in numbers:
        if n > 0: out.update({'pos' : out['pos']+1})
        if n < 0: out.update({'neg' : out['neg']+1})
        if n == 0: out.update({'zero' : out['zero']+1})
    return out

# print(pos_neg_zero(numbahs))

#Part G - 5
#Done

def main():
    # greet()
    # print_separator()
    # show_course_name()
    # greet_person('Göran')
    # introduce('Hans','Skövde')
    # print(total_area(appartment))
    # print(is_even(6))
    # print(get_larger(8,4))
    # print(classify_score(67))
    # print(full_name('Daniel','Nilsson'))
    # print(calculate_discount(500,25))
    # greeting('Ylva')
    # greeting('Francis','Howdy')
    # print(calculate_price(255))
    # print(calculate_price(500,2,10))
    # print(create_profile('Therese'))
    # print(create_profile('Urban','Umeå',False))
    # print(create_profile(city='Malmö',active=True,name='Viktoria'))
    # print(calculate_total(num))
    # print(count_even(num))
    # print(get_long_words(['Hello','Hello World','Python Rocks'],6))
    # print(find_student(students,'Bob'))
    # print(average_score(students))
    # print(*get_active_users(students), sep='\n')
    # weather_report(convert_temp(55))
    # weather_report(convert_temp(77))
    # weather_report(convert_temp(105))
    # print(final_total(items))
    # print(min_and_max(num))
    # print(palindrome('Hello'),palindrome('Anna'))
    # print(count_character_freq('Himmalaya Mountain Range'))
    # print(pos_neg_zero(numbahs))
    # print(calc_fee(18, False))
    # print(*participants,sep='\n')
    # print(calc_registration_revenue(participants))
    # print(*student_list(participants),sep='\n')
    # print(oldest_dude(participants))
    # participant_print(oldest_dude(participants))
    None

if __name__ == '__main__':
    main()