'''
Lab5 - 260915
'''

#Part A - 1
course_name = 'Python Developer AI & ML'

def course_function():
    course_name = 'Python Fundamentals'
    return course_name

# print(course_function())    #prints the local variable in the function - loval scope
# print(course_name)          #prints the global variable - global scope

#Part A - 2
def local_counter():
    count = 1

local_counter()
# print(count)    #count is a local variable accessible only in the local scope of the function.
                # not defined in global scope

#Part A - 3
global_num = 3      # global scope variable

def change_num():
    global_num = 4  # this is a different variable only with the same name. local scope variable

change_num()
# print(global_num)   #the value of the global variable is unchanged. two different variables with the same name.

#Part A - 4
def nested_numbers():
    outer_num = 5

    def inner_function():
        inner_num = 6
        print(f'Outer: {outer_num} Inner: {inner_num}') #both outer_num and inner_num are accessible from within this function

    inner_function()
    # print(inner_num)  #this wont work. enclosing scope only works down the chain

# nested_numbers()

#Part A - 5
# you should avoid naming variables that of built ins. simply avoid those generic names.
# list = [5]  #this will shadow and override the built in. avoid this.
my_list = [5]

#Part B - 1
def add_all(*numbers):
    total = 0
    for n in numbers: total += n
    return total

# print(add_all(1,2,3,4,5,6))

#Part B - 2
def average(*numbers):
    return add_all(*numbers) / len(numbers) if numbers else 0

# print(average(1,2,3,4,5,6))
# print(average())

#Part B - 3
def longest_word(*words):
    long = words[0]
    for w in words:
        if len(w) > len(long):
            long = w
    return long

# print(longest_word('Hello','Global Scope','Local Scope','Args Packing'))

#Part B - 4
def build_sentence(seperator, *words):
    return seperator.join(words)

# print(build_sentence(' ','This','is','a','sentence.'))

#Part B - 5
def describe_scores(student_name,*scores):
    return student_name, len(scores), sum(scores)/len(scores)

# print(*(describe_scores('Daniel',80,90,95,87,85)))

#Part C - 1
nums = [10,20,30]

def multi_nums(a,b,c):
    return a * b * c

# print(multi_nums(*nums))

#Part C - 2
dude = ('Daniel','Nilsson','Gothenburg')

def print_tuppli(first_name,last_name,city):
    print(first_name,last_name,city)

# print_tuppli(*dude)

#Part C - 3

def complicated_args(first,*middle,last='values'):
    print(first,middle,last)

# complicated_args('hello',1,2,3,4,last='last')
# complicated_args(1,2,3,4,last='last again')
# complicated_args('default')

#Part C - 4
# def func(*args) packs all the arguments used in the function call into local tuple args
# func(*args) unpacks the args tuple/list variable into separate arguments. 
# args = [1,2,3,4] - func(*args) == func(1,2,3,4)


#Part D - 1
def show_profile(**info):
    for key,val in info.items(): print(key,val)

info = {'name': 'Daniel', 'city' : 'Götelaborg', 'student' : True}
# show_profile(**info)
# show_profile(name='Daniel',city='Götet',student=True)

#Part D - 2
def create_user(username,**details) -> dict:
    return {'username' : username, **details}

# print(create_user('dan-nilsson',city='Gothenburg',active=True))

#Part D - 3
def build_product(name,price,**metadata) -> dict:
    return {'name' : name, 'price' : price, **metadata}
    
# print(build_product('good product', 100, good=True, productness='high'))

#Part D - 4
def not_none_settings(**settings) -> dict:
    return {s[0] : s[1] for s in settings.items() if s[1]}

# print(not_none_settings(darkmode='yes',sleep=15, ms_account=None))

#Part D - 5
args = {'name' : 'Daniel', 'student' : True, 'city' : 'Gothenburg'}

def pass_dict_args(name,city,student):
    print(name,city,student)

# pass_dict_args(**args)

#Part E - 1
def log_event(event_type, *messages, **metadata) -> dict:
    return {'event_type' : event_type, 'messages' : messages, **metadata}

# print(log_event('login attempt','login failed','incorrect password',logged=True,time='08:00'))

#Part E - 2
def calculate_order(customer,*prices,**options) -> tuple:
    discount, shipping = options['discount'] if options else 0, options['shipping'] if options else 0
    return f'Customer: {customer}', sum(prices) * (1 - discount) + shipping

# print(calculate_order('Daniel',100,200,300,500,discount=0.2,shipping=100))
# print(calculate_order('Urban',50,100,200))

#Part E - 3
def add_nums(**kwargs):
    a,b = kwargs['a'],kwargs['b']
    return a + b

def add_two_nums(a,b):
    return a + b

# print(add_nums(a=10,b=20))
# print(add_two_nums(10,20))

# no real point using kwargs if you're trying to do something simple with a fixed number and type of parameters

#Part E - 4
def make_string(*args):
    return ''.join(str(a) for a in args)

# print(make_string(1,2,3))
# print(make_string('hello',0,True,'yes'))
# print(make_string(1,2,'python',0.15,None,1,2))

#Part F - 1-5
section1 = 'Code Review Went Well. Nothing Major To Fix.'
section2 = 'Overall Looks Fine. Could Do With Some More Error Handling.'
section3 = 'The Code Structure Looks Fine. Low Code Duplication.'

sections = [{'code review' : section1}, {'bugs' : section2}, {'refactoring' : section3}]

meta_data_fields = ['author','department','version','confidential','date']

def create_report(title,*sections,**metadata) -> dict:
    return {'title' : title,'sections' : sections, **metadata}

# print(create_report('code review',*sections,confidential='yes'))

def summarize_report(report) -> str:
    title, sections = report['title'],report['sections']
    del report['title'], report['sections']
    rest = report
    return( f'Title: {title.title()}\n'+
            f'Sections: {'\n'.join(f'{list(s.keys())[0].title()} - {list(s.values())[0]}'for s in sections)}\n' +
            f'Meta: {' - '.join(f'{key}: {val}' for key, val in rest.items() if key in meta_data_fields)}'
    )
          
# print(summarize_report(create_report('code review',*sections,version='3.0',confidential='yes',nope='nope')))

def count_words(sections) -> int:
    return len(' '.join(list(s.values())[0] for s in sections).split())

# print(count_words(create_report('code review',*sections,version='3.0',confidential='yes')['sections']))

#Part F - 6

meta_data1 = {'version' : '3.5','confidential' : 'yes', 'author' : 'Daniel', 'invalid' : 'ignored'}
meta_data2 = {'department' : 'production', 'author' : 'Daniel', 'date' : '260915', 'skip' : 'yes'}

# print(summarize_report(create_report('code review',*sections,**meta_data1)))
# print(summarize_report(create_report('code review',*sections,**meta_data2)))

#Part F - 7
# summarize_report() ignores non valid meta data by : for key, val in rest.items() if key in meta_data_fields

# print(summarize_report(create_report('code review',*sections,version='3.0',confidential='yes',nope='nope')))

#Part G - 1-3
defaults = {'on' : True, 'darkmode' : True, 'charged': True}

def merge_settings(defaults,**overrides) -> dict:
    new_sett = defaults
    new_sett.update(overrides)
    return new_sett

# print(merge_settings(defaults,on=False))

def call_summary(function_name,*args,**kwargs) -> str:
    return (    f'{function_name}({','.join(f'{a}' for a in args)}' + 
                f',{','.join(f'{key}={val}' for key,val in kwargs.items())})'
    )

# print(call_summary('function_name',1,2,3,override=True,run=False,halt=True))

numbers = [10,20,50,15,18,78]

def flexible_statistics(*numbers) -> str:
    return( f'count: {len(numbers)}\n'+
            f'total: {sum(numbers)}\n'+
            f'average: {sum(numbers)/len(numbers)}\n'+
            f'min: {min(numbers)}\n'+
            f'max: {max(numbers)}'
    )

# print(flexible_statistics(*numbers))

#Part G - 4
num = 5

class Student:
    num_students = 0

    def __init__(self,name,city):
        self.name = name
        self.city = city
        Student.num_students += 1   #num_students reachable and modifiable through class.variable
        self.id = str(Student.num_students)+name.lower()

    def print_info(self):
        print(f'Name: {self.name} ID: {self.id} City: {self.city}')
        # print(num_students)   #num_students not reachable in nested function
        # print(num)            #num reachable - global scope
        # print(self.name)      #self object reachable passed in as argument - local scope
        # print(dude)           #dude reachable - global scope and assigned under function

dude = Student('Daniel','Gothenburg')

# print(Student.num_students)   #num.students inside class reachable through Student.num_students
# dude.print_info()             #class method reachable as dude.print_info()

        



