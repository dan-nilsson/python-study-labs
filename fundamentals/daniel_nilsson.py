# ==================================================
# TASK 1
# ==================================================

products = [
    {"name": "Laptop", "price": 12000, "stock": 4},
    {"name": "Mouse", "price": 350, "stock": 0},
    {"name": "Keyboard", "price": 800, "stock": 6},
    {"name": "Monitor", "price": 3200, "stock": 3},
    {"name": "Headset", "price": 950, "stock": 0},
    {"name": "Webcam", "price": 1100, "stock": 5}
]

# 1. Loop through the products.
# 2. Print the name of every product that is in stock.
# 3. Calculate the total value of all products in stock.
#    The value of a product is price * stock.
# 4. Print the total value.
# 5. Keep track of which in-stock product has the highest price
#    without using max(), and print its name.


# Write your solution below:

def products_loop(products):
    total_val,high_price,high_name = 0,0,''
    for p in products:
        if p['stock']:
            print(f'Product Name: {p['name']}')
            total_val += p['price'] * p['stock']
            if p['price'] > high_price: 
                high_name,high_price = p['name'],p['price']

    print(f'Total Value: {total_val}\nHighest Priced in stock product: {high_name}')

products_loop(products)


# ==================================================
# TASK 2
# ==================================================

scores = [78, 92, 55, 81, 67, 95, 73]

# Create a function called calculate_average that:
# - receives a list of scores
# - calculates and returns the average score
#
# Create another function called create_result that:
# - receives a list of scores
# - uses calculate_average()
# - returns "PASS" if the average is 70 or higher
# - otherwise returns "FAIL"
#
# Call create_result() using the scores above.
# Print both the average score and the final result.


# Write your solution below:

def calculate_average(scores) -> (int,float):
    return sum(scores) / len(scores)

def create_result(scores) -> str:
    return 'PASS' if calculate_average(scores) >= 70 else 'FAIL'

print(calculate_average(scores))
print(create_result(scores))


# ==================================================
# TASK 3
# ==================================================

product_prices = [250, 400, 150, 700]

order_settings = {
    "discount": 10,
    "shipping": 49,
    "priority": True
}

# Create a function called calculate_order that:
# - receives a customer name as a normal parameter
# - receives any number of product prices using *args
# - receives optional settings using **kwargs
# - calculates the subtotal of all product prices
# - applies the discount percentage if "discount" exists
# - adds shipping if "shipping" exists
# - returns a dictionary containing:
#       customer
#       subtotal
#       final_total
#       settings
#
# Call the function using:
# - customer name "Anna"
# - the values from product_prices using unpacking
# - the values from order_settings using dictionary unpacking
#
# Print the returned dictionary.


# Write your solution below:

def calculate_order(name,*args,**kwargs) -> dict:
    sub_tot = sum(args)
    discount = sub_tot * (kwargs['discount'] if kwargs['discount'] else 0) / 100
    shipping = kwargs['shipping'] if kwargs['shipping'] else 0
    fin_tot = sub_tot - discount + shipping
    return {'customer' : name, 'subtotal' : sub_tot, 'final_total' : fin_tot, 'settings' : kwargs}

print(calculate_order('Anna',*product_prices,**order_settings))


# ==================================================
# TASK 4
# ==================================================

players = [
    {"name": "  anna", "score": 85, "active": True},
    {"name": "DAVID ", "score": 72, "active": False},
    {"name": " sara ", "score": 94, "active": True},
    {"name": "LEO", "score": 67, "active": True},
    {"name": " emma", "score": 88, "active": True},
    {"name": "OSCAR ", "score": 76, "active": False}
]

# 1. Create a new list containing normalized player names.
#    Remove unnecessary whitespace and use consistent capitalization.
#    Use a list comprehension.
#
# 2. Create a new list containing only the active players
#    with a score of 80 or higher.
#    Use a list comprehension.
#
# 3. Sort the original players by score from highest to lowest.
#    Use sorted() with a lambda.
#
# 4. Print the ranking in the following format:
#
#    1. Sara - 94
#    2. Emma - 88
#    ...
#
#    Generate the ranking numbers using enumerate().
#
# 5. Create a separate list containing the player names and
#    another list containing their scores.
#    Combine them using zip() and print each name together
#    with its score.


# Write your solution below:

norm_player_names = [{key:val.strip().lower().capitalize() if isinstance(val,str) else val for key,val in d.items()} for d in players]
# print(norm_player_names)

active_80_score = [d for d in norm_player_names if d['active'] and d['score'] >= 80]
# print(active_80_score)

sorted_score = sorted(norm_player_names,key=lambda p: p['score'],reverse=True)
# print(sorted_score)

print(*[f'{i}. {d['name']} - {d['score']}' for i,d in enumerate(sorted_score,start=1)],sep='\n')

p_names = [d['name'] for d in sorted_score]
p_scores = [d['score'] for d in sorted_score]

zip_player_score = zip(p_names,p_scores)

print(*[f'Name: {'{:<8}'.format(p[0])} - Score: {p[1]}' for p in zip_player_score],sep='\n')