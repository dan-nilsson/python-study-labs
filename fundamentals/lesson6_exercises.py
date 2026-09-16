'''
Lab6 - 260916
'''

#Part A - 1
nums = [1,2,3,4,5]

def normal_squares(nums):
    out = []
    for n in nums:
        out.append(n ** 2)
    return out

def comprehension_squares(nums):
    return [n ** 2 for n in nums]

# print(normal_squares(nums))
# print(comprehension_squares(nums))

#Part A - 2
def comprehension_even():
    return [n for n in range(1,101) if n % 2 == 0]

# print(comprehension_even())

#Part A - 3
names = ['daniel nilsson  ','   eva blomström','yngve petterson   ']

def stripped_titled_names(names):
    return [name.strip().title() for name in names]

# print(stripped_titled_names(names))

#Part A - 4
scores = [90,70,80,55,65]

def passed_score(scores):
    return [score for score in scores if score >= 60]

# print(passed_score(scores))

#Part A - 5
def labeled_score(scores):
    return [(score,('PASS' if score >= 60 else 'FAIL')) for score in scores]

# print(labeled_score(scores))

#Part A - 6
#Already used comprehension in most previous labs


#Part B - 1
def map_squares(nums):
    return {num : num ** 2 for num in nums}

# print(map_squares(nums))

#Part B - 2
words = ['hello','python','is','pretty','groovy']

def map_word_len(words):
    return {word : len(word) for word in words}

# print(map_word_len(words))

#Part B - 3
dupli_words = ['one','one   ','two','two','three','THREE','four']

def set_words(words):
    return {word.strip().lower() for word in words}

# print(set_words(dupli_words))

#Part B - 4
products = [('milk',15),('eggs',30),('bread',30),('pasta',10)]

def cheap_groceries(products):
    return {key : val for key,val in products if val <= 20}

# print(cheap_groceries(products))

#Part B - 5
students = [{'name' : name, 'score' : score} for name,score in zip(stripped_titled_names(names),scores)]

def student_pass(students):
    return {s['name'] : ('PASS' if s['score'] >= 60 else 'FAIL') for s in students}

# print(student_pass(students))


#Part C - 1
songs = ['Never Gonna Give You Up','Return of the Mac','Sandstorm','Faster,Stronger,Scooter']

def playlist(songs):
    print(*[f'{i+1}. {song}' for i,song in enumerate(songs)],sep='\n')

# playlist(songs)

#Part C - 2
tasks = ['Take Attendance','Join Meeting','Take Lunch','Lab Maxxing']

def numerate_tasks(tasks):
    print(*[f'Task {i+1}: {task}' for i,task in enumerate(tasks)],sep='\n')

# numerate_tasks(tasks)

#Part C - 3
values = [100,200,500,75,80,300]

def threshold_values_indexed(values):
    print([f'Index #{i} : {val}' for i,val in enumerate(values) if val >= 100],sep='\n')

# threshold_values_indexed(values)

#Part C - 4
def range_len(nums):
    for i in range(len(nums)):
        print(f'{i} : {nums[i]}')

def enumerate_loop(nums):
    print(*[f'{i} : {num}' for i,num in enumerate(nums)],sep='\n')

# range_len(nums)
# enumerate_loop(nums)

#It's cleaner and more easy to understand that we're iterating and returning unique ordered pairs of data
#using enumerate iteration.


#Part D - 1
def zip_scores(names,scores):
    print(*[f'Name: {name} Score: {score}' for name,score in zip(names,scores)],sep='\n')

# zip_scores(stripped_titled_names(names),scores)

#Part D - 2
zipped_dict = {name.strip() : score for name,score in zip(names,scores)}
# print(zipped_dict)

#Part D - 3
product = ['laptop','phone','tv','sofa','car']
price = [15000,8000,15000,20000]
stock = [True,True,False,True,False,False,False]

combined_product = [(product,price,stock) for product,price,stock in zip(product,price,stock)]
# print(*combined_product)

#Part D - 4
def calc_what_happens(*args):
    min_zip = min([len(l) for l in args])
    max_zip = max([len(l) for l in args])
    zipped = [data for data in zip(*args)]
    zip_len = len(zipped)
    print(f'Shortest list: {min_zip} Longest list: {max_zip} Zipped length: {zip_len}')
    if zip_len == min_zip and min_zip < max_zip: print('Zip stops when the shortest list is exhausted')

# calc_what_happens(product,price,stock)

#Part D - 5
def tuple_unpack(product,price):
    return [product for product,_ in zip(product,price)]

# print(tuple_unpack(product,price))

#Part D - 6
def swap_variables():
    None


#Part E - 1
words = ['longest','long','longer','mostlongestest']

def sort_word_len(words):
    return sorted(words,key=lambda w: len(w))

# print(sort_word_len(words))

#Part E - 2
def sort_student_score(students):
    return sorted(students.items(),key=lambda s: s[1],reverse=True)

# print(*sort_student_score(zipped_dict),sep='\n')

#Part E - 3
product_dict = [{'product' : prod, 'price': price, 'stock' : stock} for prod,price,stock in zip(product,price,stock)]

def sort_product_price(products):
    return sorted(products,key=lambda p: p['price'])
    
# print(*sort_product_price(product_dict),sep='\n')

names_dicts = [ {'first_name' : 'Daniel', 'last_name' : 'Nilsson'},
                {'first_name' : 'Bob', 'last_name' : 'Builder'},
                {'first_name' : 'Linda', 'last_name' : 'Namesson'},
                {'first_name' : 'Adam', 'last_name' : 'Adamsson'}
            ]
#Part E - 4
def sort_names(names):
    return sorted(names,key=lambda p: p['last_name'])

# print(*sort_names(names_dicts),sep='\n')

#Part E - 5
def sort_normal(names):
    None


#Part F - 1
messy_products = [
    {'product_name' : 'SoFa  ', 'category' : 'FuRnItUre', 'price' : 20000, 'stock' : 15},
    {'product_name' : 'TaBlE', 'category' : 'furni TURE', 'price' : 10000, 'stock' : 15},
    {'product_name' : 'dishWASHer', 'category' : 'APPL i ANce', 'price' : 8000, 'stock' : 25},
    {'product_name' : 'stOVE', 'category' : 'appliance', 'price' : 15000, 'stock' : 25},
    {'product_name' : 'micROwaVE', 'category' : 'APPLIANCE', 'price' : 1500, 'stock' : 0},
    {'product_name' : 'BACKPACK', 'category' : 'outD O O R', 'price' : 1000, 'stock' : 250},
    {'product_name' : 'shO   ES', 'category' : 'F o o T wear', 'price' : 1000, 'stock' : 300},
    {'product_name' : 'sh I R T', 'category' : 'CLOTHES', 'price' : 500, 'stock' : 200},
    {'product_name' : 'BELT', 'category' : 'clothes', 'price' : 300, 'stock' : 150},
    {'product_name' : 'jeans', 'category' : 'clo TH ES', 'price' : 800, 'stock' : 100},
    {'product_name' : 'JaCkEt', 'category' : 'outDOOR', 'price' : 2000, 'stock' : 50},
    {'product_name' : 'UMbrELLa', 'category' : 'OUT door', 'price' : 200, 'stock' : 150}
]

#Part F - 2
'''I needed to take some fresh air after this one. Impossible is nothing'''
cleaned_products = [{key:val.replace(' ','').lower().capitalize() if isinstance(val,str) else val for key,val in d.items()} for d in messy_products]

# print(cleaned_products)

#Part F - 3
instock_products = [d for d in cleaned_products if d['stock']]

# print(instock_products)

#Part F - 4
categories = set([d['category'] for d in cleaned_products])

# print(categories)

#Part F - 5
inventory_value = {p['product_name'] : p['price'] * p['stock'] for p in instock_products}

# print(inventory_value)

#Part F - 6
sorted_by_inv_value = dict(sorted(inventory_value.items(),key=lambda item: item[1],reverse=True))

# print(sorted_by_inv_value)

#Part F - 7
ranked_invetory_value = [f'{'{:<3}'.format(i+1)}. {'{:<15}'.format(d)} : {inventory_value[d]} SEK' for i,d in enumerate(sorted_by_inv_value)]

# print(*ranked_invetory_value,sep='\n')

#Part F - 8
zipped_up = []

#Part F - 9










