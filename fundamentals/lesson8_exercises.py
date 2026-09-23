'''
Lab8 260923
'''

#Part A
class BadTeam:
    def __init__(self,name,members=[]):
        self.name = name
        self.members = members

    def add_member(self,member):
        self.members.append(member)

bad1 = BadTeam('one')
bad2 = BadTeam('two')
bad1.add_member('bob')

# print(bad1.members, bad2.members)

class CorrectTeam:
    def __init__(self,name,members=None):
        self.name = name
        if members == None: self.members = []
        else: self.members = members

    def add_member(self,member):
        self.members.append(member)

corr1 = CorrectTeam('one')
corr2 = CorrectTeam('two')
corr1.add_member('bob')

# print(corr1.members,corr2.members)

#Part B

movie = {
    'title' : 'Heat',
    'director' : 'Micheal Mann',
    'rating' : 8.7
}

class Movie:
    def __init__(self,title,director,rating):
        self.title = title
        self.director = director
        self.rating = rating

    def is_high_rating(self):
        return self.rating >= 8

movie_class = Movie('Heat','Micheal Mann',8.7)

'''
You would choose a class for when you expect to need methods for easy presentation or logic based queries on the state
It can also be used for a more secure and readable attribute mutating with setters-getters
Dict is still useful if it's a fixed data set that you expect mostly will be used to be read
'''


#Part C

class Account:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self,owner,balance,interest_rate):
        super().__init__(owner,balance)
        self.interest_rate = interest_rate

save1 = SavingsAccount('bob',100,0.015)
save2 = SavingsAccount('linda',200,0.02)

# print(save1.owner,save1.balance,save1.interest_rate)
# print(save2.owner,save2.balance,save2.interest_rate)

'''
SavingsAccount is-an Account because it uses all the base behaviour of Account and extends
on it in a meaningful way
'''

#Part D

class Employee:
    def __init__(self,name):
        self.name = name
    
    def get_information(self):
        return f'Employee Name: {self.name}'

class Developer(Employee):
    def __init__(self,name,repo):
        super().__init__(name)
        self.repo = repo

    def get_git_repo(self):
        return f'{super().get_information()} Git: {self.repo}'

class Manager(Employee):
    pass

manager = Manager('Therese')
developer = Developer('Bob','github.com/bob')

# print(manager.get_information())
# print(developer.get_git_repo())
# print(manager.get_git_repo())     #does not work - can't use methods of other sub-classes eventhough shared super-class

#Part E

class Device:
    def __init__(self,brand,year,is_active=True):
        self.brand = brand
        self.year = year
        self.is_active = is_active
        if year < 0: raise ValueError('year cannot be negative!')

class Laptop(Device):
    def __init__(self,brand,year,ram_gb,is_active=True):
        super().__init__(brand,year,is_active)
        self.ram_gb = ram_gb

class Monitor(Device):
    def __init__(self,brand,year,size,is_active=True):
        super().__init__(brand,year,is_active)
        self.size = size

laptop = Laptop('IBM',2022,32)
monitor = Monitor('Asus',2018,26)

# print(laptop.brand,laptop.year,laptop.ram_gb,laptop.is_active)
# print(monitor.brand,monitor.year,monitor.size,monitor.is_active)


#Part F

class Notification:
    def __init__(self,message):
        self.message = message

    def send(self):
        return self.message

class EmailNotification(Notification):
    def __init__(self,message,email):
        super().__init__(message)
        self.email = email

    def send(self):
        return f'Email: {self.message}'

class SMSNotification(Notification):
    def __init__(self,message,number):
        super().__init__(message)
        self.number = number

    def send(self):
        return f'SMS: {self.message}'

notis = Notification('Hello')
email = EmailNotification('Hello','bob@yahoo.com')
sms = SMSNotification('Hello','555-555111')

print(notis.send(),email.send(),sms.send())

'''
The method = sub-class if override else super-class
'''

#Part G


#Part H