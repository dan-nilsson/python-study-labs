'''
Lab5 Challenge 260918
'''
#Part 1
products = [    
    {'prod_name' : 'Laptop', 'category' : 'Tech', 'price' : 100, 'stock' : 5},
    {'prod_name' : 'Laptop', 'category' : 'Tech', 'price' : 100, 'stock' : 5},
    {'prod_name' : 'Laptop', 'category' : 'Tech', 'price' : 100, 'stock' : 5},
    {'prod_name' : 'Laptop', 'category' : 'Tech', 'price' : 100, 'stock' : 5},
    {'prod_name' : 'Laptop', 'category' : 'Tech', 'price' : 100, 'stock' : 5},
    {'prod_name' : 'Laptop', 'category' : 'Tech', 'price' : 100, 'stock' : 5},
    {'prod_name' : 'Laptop', 'category' : 'Tech', 'price' : 100, 'stock' : 5},
    {'prod_name' : 'Laptop', 'category' : 'Tech', 'price' : 100, 'stock' : 5}
]

customers = [
    {'name' : 'Anders', 'email' : 'anders@saab.se', 'customer_id' : 'and123', 'year_total' : 0},
    {'name' : 'Chandler', 'email' : 'chandler@statestreet.com', 'customer_id' : 'cha123', 'year_total' : 0},
    {'name' : 'Lisa', 'email' : 'lisa@volvo.se', 'customer_id' : 'lis123', 'year_total' : 0},
    {'name' : 'Emma', 'email' : 'emma@astrazeneca.se', 'customer_id' : 'emm123', 'year_total' : 0},
    {'name' : 'Jimmy', 'email' : 'jimmy@abb.se', 'customer_id' : 'jim123', 'year_total' : 0},
]

#Part 2

def create_order(order_id, customer, *args, **kwargs) -> dict:
    return {'order_id' : order_id, 'customer' : customer, 'products' : args, 'options' : kwargs}


#Part 3

def calc_subtotal(*args) -> float:
    return sum(args)

#Part 4

def optional_order_settings(**kwargs) -> dict:
    return {key:val for key,val in kwargs if val}

#Part 5

#Part 6

def order_summary(order,customer,*args,**kwargs) -> [str]:
    return( f'ORDER SUMMARY',
            f'Order ID: {order}',
            f'Customer: {customer}',
            f'Messages/Notes: {' - '.join(args)}',
            f'Metadata: {' - '.join(kwargs)}'
    )

#Part 7

store_name = 'Big Ol\' Store'
tax_rate = 25

def set_tax_rate() -> list:
    tax_rate = 20
    return store_name,tax_rate

# print(tax_rate)
store_name,tax_rate = set_tax_rate()
# print(store_name,tax_rate)

#Part 8

def process_order(order):
    subtotal = calc_subtotal(*order['products'])
    metadata = order['metadata']
    discount = metadata['discount'] if metadata['discount'] else 0
    shipping = metadata['shipping'] if metadata['shipping'] else 0
    finaltotal = subtotal - (subtotal * discount) + shipping
    return subtotal,discount,shipping,finaltotal

#Part 9

#Part Final

def daily_order_report(report_title) -> [str]:
    return( f'{report_title}',
            f'Numbers of orders: {100}',
            f'Total Revenue: {20000}',
            f'Average Order Value: {200}',
            f'Largest Order: {2000}',
            f'Smallest Order: {100}',
            f'DAILY ORDER REPORT',
            f'DAILY ORDER REPORT',
            f'DAILY ORDER REPORT',
            f'DAILY ORDER REPORT',
            f'DAILY ORDER REPORT',
            f'DAILY ORDER REPORT',
            f'DAILY ORDER REPORT'
    )









