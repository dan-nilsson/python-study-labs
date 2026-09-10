'''
Lab 2 - 260909
'''
#Part A - 1
prog_langs = ['Python','Java','C','C#','JavaScript','Go','Erlang','Haskell']

def prog_langs_index():
    print(  f'{prog_langs[0]}\n'    #first
            f'{prog_langs[-1]}\n'   #last   
            f'{prog_langs[2]}\n'    #third
            f'{prog_langs[-2]}'     #second to last
        )
# prog_langs_index()

#Part A - 2
def prog_langs_slice():
    print(  f'{prog_langs[-2:]}\n'  #list of last 2 ele
            f'{prog_langs[::2]}\n'  #list of every other ele   
            f'{prog_langs[:2]}\n'   #list of first 2 ele
            f'{prog_langs[::-1]}'   #list in reverse
        )
# prog_langs_slice()

#Part A - 3 
def prog_lang_operators():
    print(prog_langs)
    prog_langs.append('Pascal')
    print(prog_langs)
    prog_langs.insert(2,'C++')
    print(prog_langs)
    pop = prog_langs.pop()
    print(prog_langs)
    print(pop)
# prog_lang_operators()

#Part A - 4
nums = [1,2,3,4,5,6]
def list_operations():
    length = len(nums)
    min_val = min(nums)
    max_val = max(nums)
    sum_val = sum(nums)
    print(f'len: {length} min: {min_val} max: {max_val} sum: {sum_val}')
# list_operations()

#Part A - 5              
    
def sort_sorted():
    a = [4,3,1,5,2]
    b = [5,1,3,4,2]   
    sorted_b = sorted(b)    #returns a new sorted list
    print(f'a: {a}\nb: {b}\nsorted b: {sorted_b}') 
    a.sort()                #assigns a to a sorted list
    a.reverse()
    print('a-reverse: ',a)
# sort_sorted()
    

#Part A - 6
def pointers_questionmark():
    a = [4,3,1,5,2]
    b = [5,1,3,4,2] 
    print(a, b)
    a, b = b, a         #reverses the object the variables reference. done in one snapshot so not in-line
    print(a, b)
    a = b.copy()        #reassigns a to a new copy of the object b variable was reference to
    print(a,b)
# pointers_questionmark()

#Part B - 1
def rgb_tuple():
    rgb = (255,255,255)
    r,g,b = rgb
    print(f'r: {r} g: {g} b: {b}')
# rgb_tuple()

#Part B - 2
def tuple_unpack():
    person = ('Nikola', 31, 'Denver')
    n,a,c = person
    print(f'Name: {n} Age: {a} City: {c}')
# tuple_unpack()

#Part B - 3
#Since tuples usually contain mixed types in a certain pattern order it's best to keep immutable.

#Part B - 4
def tuple_coords():
    coords = [(10,20),(20,30),(30,40),(40,50)]
    print(f'first coords X: {coords[0][0]} Y: {coords[0][1]}')
# tuple_coords()

#Part C - 1
def set_duplicates():
    courses = ['Python & AI', 'IT-Helpdesk', '.NET Fullstack']
    courses_dupli = courses * 3
    courses_set = set(courses_dupli)
    print(f'Duplicates List: {len(courses_dupli)}\nUniques Set: {len(courses_set)}')
# set_duplicates()

#Part C - 2
def set_operators():
    dev1_skills = {'Java','Git','Agile','Python'}
    dev2_skills = {'Python', 'Git', 'JavaScript','Haskell'}
    print(  f'Shared skills: {dev1_skills & dev2_skills}\n'
            f'Only Dev1 skills: {dev1_skills - dev2_skills}\n'
            f'All skills: {dev1_skills | dev2_skills}\n'
        )
# set_operators()

#Part C - 3
def set_functions():
    stuff = {1,2,3,4,5,6}
    print(stuff)
    stuff.add(5)
    print(stuff) #no change
    stuff.add(7)
    print(stuff) #ele added
    stuff.remove(1)
    print(1 not in stuff) #ele 1 removed
# set_functions()

#Part C - 4
# If your collecting emails in your organization to send information and people might have department database
# overlap. To ensure not sending these people duplicates.

#Part D - 1
laptop = {
    'brand'     : 'IBM',
    'model'     : 'T440',
    'RAM'       : 32,
    'storage'   : 1024,
    'price'     : 3000
}
def dict_laptop():
    print(  f'Brand: {laptop['brand']} Model: {laptop['model']}\n'
            f'RAM: {laptop['RAM']} Storage: {laptop['storage']} Price: {laptop['price']}'
        )
# dict_laptop()

# Part D - 2
def dict_laptop_update():
    lap = dict(laptop)
    lap.update({'price':3000,'os':'linux'})
    del lap['storage']
    print(f'New price: {lap['price']} Operating System: {lap['os']} Storage key?: {lap.get('storage')}')
# dict_laptop_update()

#Part D - 3
def dict_operators():
    price = laptop.get('price')
    missing = laptop.get('colour')
    print(f'KEY: {price} MISSING: {missing}')
# Dictionary is a good datatype for lookup knowing only key 'phrase'
# It's the same thing as 2 lists finding ele key in first and matching index
# This is just a more convenient and clearer representation

# dict_operators()

#Part D - 4
def dict_operators_print():
    print(  f'Keys: {laptop.keys()}\n'
            f'Vals: {laptop.values()}\n'
            f'Pairs: {laptop.items()}'        
    )
# dict_operators_print()

#Part D - 5
def dict_course_hours():
    hours = {'Python & AI' : 500, 'IT-Helpdesk' : 100, '.NET Fullstack' : 100}
    print(f'Hours total: {sum(hours.values())}')
# dict_course_hours()

#Part E - 1-3
books = [
    {'title' : 'Pride and Prejudice', 'author' : 'Jane Austen', 'pages' : 300, 'availible' : True},
    {'title' : 'The Great Gatsby', 'author' : 'F. Scott Fitzgerald', 'pages' : 180, 'availible' : True},
    {'title' : 'To Kill a Mockingbird', 'author' : 'Harper Lee', 'pages' : 281, 'availible' : True},
    {'title' : 'Moby Dick', 'author' : 'Herman Melville', 'pages' : 585, 'availible' : True},
    {'title' : '1984', 'author' : 'George Orwell', 'pages' : 328, 'availible' : True}
]
def nested_collections():
    print(f'Title 3rd book: {books[2]['title']}\nAvailability 5th book: {books[4]['availible']}')
    books[4]['title'] = 'Hmmm'
    books[4]['fiction'] = False
    print(f'Updated title: {books[4]['title']}\nNew key: {books[4].items()}')
# nested_collections()

#Part E - 4
def dict_departments():
    company = {
        'production' : ['Bob','Eric','Linda','Gregory','Sam'],
        'sales' : ['Henric','Camilla','Sandra'],
        'management' : ['Jim','Frank']
    }
    print(  f'Number of employees by department -\nProduction: {len(company['production'])} '
            f'Sales: {len(company['sales'])} Management: {len(company['management'])}'
    )
# dict_departments()
    
#Part E - 5
def dict_courses():
    courses = [ 
        {'name' : 'Python & AI', 'teacher' : 'Haithem', 'topics' : ['Fundamentals','SQL Databases','Data Analasys','ML & DL']},
        {'name' : 'IT-Helpdesk', 'teacher' : 'Bob', 'topics' : ['Microsoft Suite','Work Process','Customer Handling','Technical Base']},
        {'name' : '.NET Fullstack', 'teacher' : 'Michael', 'topics' : ['.NET','JavaScript','Backend','Deployment']}
    ]
    print(f'Python course curriculum: {', '.join(courses[0].get('topics'))}')
# dict_courses()

#Part F - 1-6
def personal_media_catalouge():
    movies = [
        {'title' : 'Heat', 'director' : 'Michael Mann', 'year' : 1995, 'genre' : 'Heist', 'rating' : 8.3},
        {'title' : 'The Godfather', 'director' : 'Francis Ford Coppola', 'year' : 1972, 'genre' : 'Drama', 'rating' : 9.2},
        {'title' : 'Leon : The Professional', 'director' : 'Luc Besson', 'year' : 1994, 'genre' : 'Drama',  'rating' : 8.5},
        {'title' : 'Das Boot', 'director' : 'Wolfgang Pettersen', 'year' : 1981, 'genre' : 'War',  'rating' : 8.3},
        {'title' : 'Reservoir Dogs', 'director' : 'Quintin Tarantino', 'year' : 1992, 'genre' : 'Thriller',  'rating' : 8.2},
        {'title' : 'Full Metal Jacket', 'director' : 'Stanley Kubrick', 'year' : 1987, 'genre' : 'War',  'rating' : 8.2},
        {'title' : 'Snatch', 'director' : 'Guy Ritchie', 'year' : 2000, 'genre' : 'Comedy',  'rating' : 8.2},
        {'title' : 'Die Hard with a Vengeance', 'director' : 'John McTiernan', 'year' : 1995, 'genre' : 'Action',  'rating' : 7.6},
    ]
    genres = set([d.get('genre') for d in movies])
    print(genres)
    movie_tuples = [(d.get('title'), d.get('year')) for d in movies]
    print(movie_tuples, end='\n')

    for m in movies:
        for key,val in m.items():
            print(f'{key}: {val}',end=' ')
        print()   

# personal_media_catalouge()

#Part G - 1
def unique_users():
    users_a = ['Bob', 'Linda', 'Eric', 'Jimmy', 'Stephen', 'Emily']
    users_b = ['Linda', 'Henric', 'Gregory', 'Jimmy', 'Frank', 'Bob']

    duplicates = set(users_a).intersection(set(users_b))
    print(duplicates)
    all_users = set(users_a).union(set(users_b))
    unique = all_users.difference(duplicates)
    print(unique)
# unique_users()

#Part G - 4
'''
List is a good generic data structure for multiple elements
Tuple is a less complex Dictionary where you don't need key lookup but is used much in the same manner
- where formatting determines field 'key'
Set is a good way to store unique values where order/indexing doesn't matter
Dictionary is a good data structure for more complex key-word type entries.
- Often with same formatting where each dictionary is a multiple field data point
'''

