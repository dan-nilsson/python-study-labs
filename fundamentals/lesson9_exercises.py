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

print(*[pd.display_status() for pd in printer_displays],sep='\n')

'''
You can call methods on various different types regardless as long as they have the needed behaviour.
As long as they all quack.
'''

#Part D


#Part E


#Part F


#Part G


#Part H