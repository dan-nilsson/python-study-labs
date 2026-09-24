'''
Lab10 260924
(we don't talk about Lab9)
'''

#Part A
class EmailNotification:
    def __init__(self,message):
        self.message = message

    def send(self):
        return 'Email Sent: '+self.message

class SMSNotification:
    def __init__(self,message):
        self.message = message

    def send(self):
        return 'SMS Sent: '+self.message

class PushNotification:
    def __init__(self,message):
        self.message = message
        
    def send(self):
        return 'Push Sent: '+self.message

notis = [
    EmailNotification('hey'),
    SMSNotification('hey'),
    PushNotification('hey')
]

# print(*[n.send() for n in notis],sep='\n')

'''
As long as they have implementation of the method class doesn't matter
'''

#Part B

class Document:
    def __init__(self,title):
        self.title = title

    def describe(self):
        return f'This is a document with the title: {self.title}'

class PDFDocument(Document):
    def describe(self):
        return f'This is a PDF document with the title: {self.title}'

class TextDocument(Document):
    def describe(self):
        return f'This is a Text document with the title: {self.title}'

documents = [
    PDFDocument('taxes'),
    PDFDocument('mortgage'),
    PDFDocument('stocks'),
    TextDocument('movie plot'),
    TextDocument('to-do list')
]

# print(*[d.describe() for d in documents],sep='\n')

#Part C

class Printer:
    def __init__(self,brand):
        self.brand = brand

    def display_status(self):
        return 'POWER : ON'

class Display:
    def __init__(self,brand):
        self.brand = brand

    def display_status(self):
        return 'POWER : ON'

printer_displays = [Printer('Canon'),Display('Asus'),Printer('HP'),Display('LG')]

# print(*[pd.display_status() for pd in printer_displays],sep='\n')

'''
You can call methods on various different types regardless as long as they have the needed behaviour.
As long as they all quack.
'''

#Part D

class User:
    def __init__(self,name):
        self.name = name

class AdminUser(User):
    pass

admin = AdminUser('Bob')

# print(isinstance(admin,AdminUser),isinstance(admin,User),isinstance(admin,str))

'''
The object instance admin is both it's distinct sub-class AdminUser aswell as it's super-class User
'''

#Part E

class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'Product Name: {self.name} Price: {self.price}'

prod = Product('Good',100)

# print(prod)     # <__main__.Product object at 0x7fcac51916a0>

products = [Product('Bike',10000),Product('Car',300000),Product('Truck',400000)]

# print(*[p for p in products],sep='\n')

prod_str = str(prod)

# print(type(prod_str),isinstance(prod_str,str))

#Part F

class Account:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f'Account Owner: {self.owner} Account Balance: {self.balance}'

class SavingsAccount(Account):
    def __init__(self,owner,balance,interest_rate):
        super().__init__(owner,balance)
        self.interest_rate = interest_rate

    def __str__(self):
        return f'{super().__str__()} Interest Rate: {self.interest_rate}'

acc = Account('Bob',5000)
saveacc = SavingsAccount('Linda',8000,0.15)

# print(acc,saveacc,sep='\n')

#Part G

class CPU:
    def __init__(self,brand):
        self.brand = brand

class Computer:
    def __init__(self,brand,cpu):
        self.brand = brand
        self.cpu = cpu

cpu = CPU('Intel')
computer = Computer('IBM',cpu)

# print(computer.brand,computer.cpu.brand)

'''
Computer has-a CPU makes more sense since they wont share all behaviour
'''

'''
Car/Engine - composition. Car has-a Engine
Manager/Employee - both/depends, Manager is-a Employee, but also Manager has-a Employee
- in the sense that they manage the Employee.
- would both be sub-class Employee with attribute list of managed Employee
Course/Teacher - composition - Course has-a Teacher
Phone/Device - inheritence - Phone is-a Device
 '''

#Part H

data = 'bish bash bosh'

class Exporter:
    def __init__(self,path):
        self.path = path

    def export(self,data):
        return f'Standard Export: {data}'

    def __str__(self):
        return f'Exporter'

class ConsoleExporter(Exporter):
    def export(self,data):
        return f'Console: {data}'

    def __str__(self):
        return f'Console Exporter'

class TextExporter(Exporter):
    def export(self,data):
        return f'Text: {data}'

    def __str__(self):
        return f'Text Exporter'

class SummaryExporter(Exporter):
    def export(self,data):
        return f'Summary: {data}'

    def __str__(self):
        return f'Summary Exporter'

exporters = [
    Exporter(),
    ConsoleExporter(),
    TextExporter(),
    SummaryExporter()
]

# print(*[e for e in exporters],sep='\n')
# print(*[e.export(data) for e in exporters],sep='\n')

class NotExporter:
    def __init__(self):
        pass

    def export(self,data):
        return f'Not Exporter: {data}'

notexp = NotExporter()

# print(*[e.export(data) for e in exporters],notexp.export(data),sep='\n')
# print(*[isinstance(e,Exporter) for e in exporters],isinstance(notexp,Exporter),sep='\n')

class FilePath:
    def __init__(self,path):
        self.path = path

'''
I couldn't think of a good composition.
We're just going to have to pretend this was a great idea.
'''
