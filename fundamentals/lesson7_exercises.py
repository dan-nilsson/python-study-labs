'''
Lab7 260922
'''

#Part A 1

class Book:
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    def islong(self):
        return self.pages > 300

book1 = Book('good book','good author',540)
book2 = Book('so-so book','so-so author',540)
book3 = Book('groovy book','groovy author',540)
book4 = Book('mediocre book','mediocre author',540)

# print(book1.title,book1.author,book1.pages)
# print(book2.title,book2.author,book2.pages)
# print(book3.title,book3.author,book3.pages)
# print(book4.title,book4.author,book4.pages)

#Part A 2

class Laptop:
    def __init__(self,brand,model,ram_gb,price):
        self.brand = brand
        self.model = model
        self.ram_gb = ram_gb
        self.price = price

lap1 = Laptop('IBM','ThinkPad',32,15000)
lap2 = Laptop('Apple','MacBook Pro',32,35000)
lap3 = Laptop('Dell','XPS',32,25000)

lap3.price = 22000

# print(lap1.price,lap2.price,lap3.price)

#Part A 3

lap4 = Laptop('IBM','ThinkPad',16,10000)
lap5 = Laptop('IBM','ThinkPad',16,10000)

# print(lap4 == lap5, lap4 is lap5)

#Part A 4-5

class Default:
    def __init__(self,value=1,string='yes',logic=False):
        self.value = value
        self.string = string
        self.logic = logic

default = Default()
# print(default.value,default.string,default.logic)

default2 = Default(logic=True,string='no',value=255)
# print(default2.value,default2.string,default2.logic)


#Part B 1

longbook = Book('long','book',301)
# print(longbook.islong())

#Part B 2-3

class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(self,deposit):
        self.balance += deposit

    def withdraw(self,amount):
        if amount > self.balance: raise ValueError('Insufficient Funds')
        self.balance -= amount

freddiemac = BankAccount('freddie',5000)
freddiemac.deposit(4000)
# print(freddiemac.balance)
# print(freddiemac.withdraw(10000))

#Part B 4

class Task:
    def __init__(self,title,completed=False):
        self.title = title
        self.completed = completed

    def complete(self):
        self.completed = True

    def reopen(self):
        self.completed = False

task1 = Task('Complete Lab7')
# print(task1.completed)
task1.complete()
# print(task1.completed)
task1.reopen()
# print(task1.completed)

#Part B 5

task2 = Task('First Task')
task3 = Task('Second Task')
task2.complete()
# print(task2.title,task2.completed,task3.title,task3.completed)

#Part C 1-6

class Product:
    tax_rate = 0.25

    def __init__(self,name,price):
        self.name = name
        self.price = price

    def price_with_tax(self):
        return self.price * (1 + self.tax_rate)

prod1 = Product('Laptop',20000)
prod2 = Product('Coffe Maker',1500)
prod3 = Product('Keyboard',800)

# print(prod1.price_with_tax(),prod2.price_with_tax(),prod3.price_with_tax())
Product.tax_rate = 0.35
# print(prod1.price_with_tax(),prod2.price_with_tax(),prod3.price_with_tax())
prod3.tax_rate = 0.45
# print(prod1.price_with_tax(),prod2.price_with_tax(),prod3.price_with_tax())
# print(Product.tax_rate)
# print(prod3.tax_rate)

#Part D 1-6

class Student:
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def get_status(self):
        return 'PASS' if self.score >= 70 else 'FAIL'

students = [
    Student('Bob',100),
    Student('Lisa',69),
    Student('Mike',55),
    Student('Harald',90),
    Student('Håkan',78),
    Student('Ylva',95)
]

# print(*[f'{s.name} {s.score}' for s in students],sep='\n')
# print(*[f'{s.name} {s.get_status()}' for s in students],sep='\n')
# 
# print(*[f'{s.name}' for s in students if s.get_status() == 'PASS'])

#Part E 1-7

class Teacher:
    def __init__(self,name):
        self.name = name

class Course:
    students = []

    def __init__(self,name,teacher):
        self.name = name
        self.teacher = teacher
    
    def add_student(self,student):
        self.students.append(student)

teacher = Teacher('Göran')
course = Course('Python for Dummies',teacher)
# print(course.name,course.teacher.name)

for s in students: course.add_student(s)
# print(*[s.name for s in course.students])

#Part F 1   




#Part F


#Part G