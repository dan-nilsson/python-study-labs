'''
Lab 3 - 260910
'''

#Part A - 1
def num_posnegzero(num):
    if num == 0:
        return 'Number is zero'
    elif num > 0:
        return 'Number is positive'
    else:
        return 'Number is negative'
# print(num_posnegzero(5),num_posnegzero(0),num_posnegzero(-1),sep='\n')

#Part A - 2
def classify_age(age):
    if age < 13:
        return 'You are a young child'
    elif age in range (13,20):
        return 'You are a teenager'
    elif age in range(20,30):
        return 'You are in your twenties'
    else:
        return 'Age is only a number'
# print(classify_age(10),classify_age(19),classify_age(25),classify_age(41),sep='\n')
# print(classify_age(int(input('Enter your age: '))))

#Part A - 3
def login(u,p):
    stored_u = 'bob'
    stored_p = 'pass123'
    if u == stored_u:
        if p == stored_p:
            return 'You have logged in succesfully!'
        else:
            return 'Incorrect password!'
    else:
        return 'Invalid username!'
# print(login(input('Username: '),input('Password: ')))

#Part A - 4
def grade(score):
    if score >= 90:
        return 'Grade A'
    elif score >= 80:
        return 'Grade B'
    elif score >= 70:
        return 'Grade C'
    elif score >= 50:
        return 'Grade D'
    else:
        return 'Grade F'
# print(grade(100),grade(49))

#Part A - 5
def free_shipping(total,is_memb=False):
    if is_memb and total >= 200:
        return True
    elif total >= 500:
        return True
    else:
        return False
# print(free_shipping(100,True), free_shipping(250,True), free_shipping(700))

#Part A - 6
def one_does_not_simply_boolean():
    print(  5 == 5,     #True
            5 != 2,     #True
            3 > 1,      #True
            3 < 1,      #False
            5 >= 4,     #True
            5 <= 3,     #False
            sep='\n'
    )
# one_does_not_simply_boolean()

#Part B - 1
def truthy_falshy(input):
    return bool(input)
# print(truthy_falshy(''),truthy_falshy(' '),truthy_falshy([]),truthy_falshy([1]),
    # truthy_falshy(0),truthy_falshy(1),sep='\n')

#Part B - 2
def supported_lang(lang):
    supported = ['English','Swedish','German','Spanish']
    return lang in supported
# print(supported_lang('English'),supported_lang('Danish'))

#Part B - 3
def blocked_users(user):
    blocked = ['greg','hans','drew']
    return user not in blocked
# print(blocked_users('greg'), blocked_users('daniel'))

#Part B - 4
def readable_not():
    return 5 not in [1,2,3] and not (not 'hey') #not very readable
# print(readable_not())

#Part C - 1
def numbered_greeting():
    people = ['Hans','Greg','Bob','Frank','Mona']
    print('\n'.join([f'Welcome {person}, you are guest #{i+1}!' for i,person in enumerate(people)]))
# numbered_greeting()

#Part C - 2
def print_even():
    for n in range(1,51):
        if n % 2 == 0:
            print(n)
# print_even()

#Part C - 3
nums = [1,2,3,4,5,6,7]
def calc_sum():
    
    sum = 0
    for n in nums:
        sum += n
    return sum
# print(calc_sum())

#Part C - 4
def max_num():
    max = 0
    for n in nums:
        if n > max:
            max = n
    return max
# print(max_num())

#Part C - 5
def five_chars():
    words = ['Hello','Goodbye','Longword','No','Yes']
    count = 0
    for w in words:
        if len(w) >= 5:
            count += 1
    return count
# print(five_chars())

#Part C - 6
def count_passing_grade():
    scores = [90,70,80,65,50]
    count = 0
    for s in scores:
        if s >= 70:
            count += 1
    return count
# print(count_passing_grade())

#Part C - 7
def loop_dict():
    dude = {'name' : 'Bob', 'age' : 30, 'awesome' : True}
    for key in dude.keys():
        print(key)
    for val in dude.values():
        print(val)
    for item in dude.items():
        print(item)
# loop_dict()

#Part D - 1
def print_ten_reverse():
    nums = list(range(1,11))
    while nums:
        print(nums.pop())
# print_ten_reverse()

#Part D - 2
def multiplication_table(num):
    for n in range(11):
        print(f'{num} x {n} = {num*n}')
# multiplication_table(5)

#Part D - 3
def playlist():
    songs = ['Song','Songer','Songest','Mostly Song']
    for i,s in enumerate(songs):
        print(f'{i+1}. Title: {s} Artist: Rick Astley')
# playlist()

#Part D - 4
def print_coords():
    for x in range(1,4):
        for y in range(1,5):
            print(f'X: {x}, Y: {y}')
# print_coords()

#Part D - 5
def print_grid():
    for row in range(1,6):
        for col in range(1,6):
            print(col,end=' ')
        print()
# print_grid()

#Part E - 1
def countdown():
    for n in range(10,0,-1):
        print(n)
    print('lift-off')
# countdown()

#Part E - 2
def pass_word():
    pword = 'pass123'
    while True:
        if input('Enter password: ') == pword:
            print('Correct password!')
            break
        print('Wrong password!')
# pass_word()

#Part E - 3
def print_menu():
    while True:
        print(f'1. Information\n2. Other Option\n3. More Stuff\n4. Quit')
        if input('Select an option (1-4): ') == '4':
            break
# print_menu()

#Part E - 4
def userinput_sum():
    sum = 0
    while True:
        num = int(input('Enter a number to add to sum. 0 to quit.'))
        if num == 0:
            print(f'The sum of entered numbers is : {sum}')
            break
        sum += num
# userinput_sum()

#Part E - 5
def guess_secretnum():
    secretnum = 7
    while True:
        if int(input('Guess the secret number:')) == secretnum:
            print(f'You guessed the secret number {secretnum} correctly!')
            break
        print(f'Wrong guess.')
# guess_secretnum()

#Part F - 1
def div_by_7_9():
    for n in range(1,101):
        if n % 7 == 0 and n % 9 == 0:
            print(f'The number {n} is divisable by both 7 & 9!')
            break
# div_by_7_9()

#Part F - 2
def skip_empty():
    strings = ['Hey','Hello','Word','','Skipped?']
    for s in strings:
        if s == '':
            continue
        print(s)
# skip_empty()

#Part F - 3


#Part F - 4
def find_999():
    nums = [1,-5,7,999,-4,8]
    for n in nums: 
        if n < 0:
            continue
        if n == 999:
            print(n,'found it')
            break
        print(n)
# find_999()

#Part H - 1
def fizzbuzz():
    for n in range(1,101):
        if n % 3 == 0:
            if n % 5 == 0:
                print(f'{n}. FizzBuzz')
                continue
            print(f'{n}. Fizz')
        elif n % 5 == 0:
            print(f'{n}. Buzz')
# fizzbuzz()

#Part H - 2
def count_vowels(sentence):
    vowels = 'aeiou'
    count = 0
    for char in sentence:
        if char in vowels:
            count += 1
    return count
# print(count_vowels(input('Enter a sentence to count vowels: ')))

#Part H - 3
def find_dupli():
    None

#Part H - 4
def histogram():
    nums = [3,5,2]
    for n in nums:
        print('*'*n)
# histogram()


        
        

        
