'''
Lab5 Challenge 260918
'''
#Part 1
products = [    
    {'prod_name' : 'Laptop', 'category' : 'Tech', 'price' : 20000, 'stock' : 5},
    {'prod_name' : 'Monitor', 'category' : 'Tech', 'price' : 5000, 'stock' : 5},
    {'prod_name' : 'Printer', 'category' : 'Tech', 'price' : 4000, 'stock' : 5},
    {'prod_name' : 'Server', 'category' : 'Tech', 'price' : 80000, 'stock' : 5},
    {'prod_name' : 'Switch', 'category' : 'Tech', 'price' : 3000, 'stock' : 5},
    {'prod_name' : 'Desktop', 'category' : 'Tech', 'price' : 30000, 'stock' : 5},
    {'prod_name' : 'VR Headset', 'category' : 'Tech', 'price' : 10000, 'stock' : 5},
    {'prod_name' : 'Projector', 'category' : 'Tech', 'price' : 15000, 'stock' : 5}
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
    return {'order_id' : order_id, 'customer' : customer, 'products' : [*args], 'options' : kwargs}

orders = [
    create_order('ORD-4523','and123','Laptop','Laptop','Laptop','Printer',discount=10,shipping='express'),
    create_order('ORD-6745','cha123','Desktop','Monitor',discount=10,shipping='express'),
    create_order('ORD-7812','lis123','Server','Switch',discount=10,shipping='express'),
    create_order('ORD-8945','emm123','Desk','Chair',discount=10,shipping='express'),
    create_order('ORD-1289','jim123','Projector','VR Headset',discount=10,shipping='express')
]
# print(orders)


#Part 3

def calc_subtotal(*args) -> float:
    prices = [[p['price'] for p in products if p['prod_name'] == o] for o in args]
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

order = orders[1]
# print(*order_summary(order['order_id'],order['customer'],*order['products'],**order['options']),sep='\n')

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

def process_order(order) -> dict:
    order_prices = [p['price'] for p in products for o in order['products'] if p['prod_name'] == o]
    subtotal = calc_subtotal(*order_prices)
    metadata = order['options']
    discount = metadata.get('discount',0)
    shipping = metadata.get('shipping','standard')
    shipping_cost = 500 if shipping == 'express' else 200
    finaltotal = subtotal - (subtotal * (discount / 100)) + shipping_cost
    process_data = {'subt' : subtotal, 'disc' : discount, 'ship' : shipping_cost, 'total' : finaltotal}
    out_dict = order.copy()
    out_dict.update(process_data)
    return out_dict


# print(process_order(order))

#Part 9

orders = orders + [
    create_order('ORD-7823','and123','Desk','Desk','Chair',discount=10,shipping='express'),
    create_order('ORD-7834','cha123','Monitor',shipping='express'),
    create_order('ORD-7867','jim123','Desktop',discount=20,instructions='ask for Hank'),
    create_order('ORD-7867','cha123','Projector','Printer',discount=20,instructions='leave at front desk')
]
# print(orders)

#Part Final

def daily_order_report(report_title) -> [str]:
    all_processed_order = [process_order(o) for o in orders]
    all_total_prices = [o['total'] for o in all_processed_order]
    orders_customer = [o['customer'] for o in orders]
    customer_order_count = {c:orders_customer.count(c) for c in orders_customer}
    customer_id_most_orders = max(customer_order_count,key=lambda k: customer_order_count[k])
    return[ f'{report_title}',
            f'Numbers of orders: {len(orders)}',
            f'Total Revenue: {sum(all_total_prices)}',
            f'Average Order Value: {sum(all_total_prices) / len(all_total_prices)}',
            f'Largest Order: {max(all_total_prices)}',
            f'Smallest Order: {min(all_total_prices)}',
            f'Customer with the most orders: {max([c['name'] if c['customer_id'] == customer_id_most_orders else '' for c in customers])}',
            f'With {customer_order_count[customer_id_most_orders]} orders.'
    ]

# print(*daily_order_report('BIG \'OL STORE DAILY REORT'),sep='\n')

def flexible_report_system(title,*args,**kwargs) -> [str]:
    return [
        '-' * len(title),
        title,
        '-' * len(title),
        *args,
        *[f'{key} : {val}' for key,val in kwargs.items()]
]

# print(*flexible_report_system('Report Test Title','First Section','Second Section',version='0.5.5',date='1995-04-10'),sep='\n')
    









