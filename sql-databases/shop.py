import sqlite3
import os.path #database read wouldn't work without path

base_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(base_dir, 'webshop.db')

def connect():
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def list_products(conn):
    cursor = conn.execute("SELECT product_id, name, price, stock FROM products")
    for pid, name, price, stock in cursor.fetchall():
        print(f"{pid:>3}  {name:<20} {price:>8.2f} kr  ({stock} in stock)")

def search_customers(conn):
    city = input("City: ")
    cursor = conn.execute(
        "SELECT first_name, last_name FROM customers WHERE city = ?", (city,))
    rows = cursor.fetchall()
    if not rows:
        print("No customers found.")
    for first, last in rows:
        print(first, last)

def add_product(conn):
    name = input("Name: ")
    category = input("Category: ")
    price = float(input("Price: "))
    stock = int(input("Stock: "))
    conn.execute(
        "INSERT INTO products (name, category, price, stock) VALUES (?, ?, ?, ?)",
        (name, category, price, stock))
    conn.commit()
    print("Saved!")

def change_stock(conn):
    product_id = input("Product-ID: ")
    stock = int(input("Stock: "))
    conn.execute(
        "UPDATE products SET stock = ? WHERE product_id = ?",
        (stock, product_id))
    conn.commit()
    print("Saved!")

def get_receipt(conn):
    order_id = int(input("Order-ID: "))
    cursor = conn.execute(
        "SELECT p.name, oi.quantity, (oi.quantity * oi.unit_price) AS line_total "
        "FROM order_items oi "
        "JOIN products p ON oi.product_id = p.product_id "
        "WHERE oi.order_id = ?", (order_id,))
    conn.commit()
    data = cursor.fetchall()
    lines = [ f'{i}. {name:<20} x{quantity:>3} : {line_total:.2f} SEK' 
            for i,(name,quantity,line_total) in enumerate(data,1)]
    order_total = sum([line_total for (n,q,line_total) in data])
    print('RECEIPT:',*lines,f'TOTAL: {order_total} SEK',sep='\n')

def best_sellers(conn):
    cursor = conn.execute(
        "SELECT p.name, COUNT(oi.product_id) AS sold "
        "FROM order_items oi "
        "JOIN products p ON oi.product_id = p.product_id "
        "GROUP BY p.name "
        "ORDER BY sold DESC LIMIT 3")
    conn.commit()
    lines = [f'{i}. {name:<20} {sold:>3}' for i,(name,sold) in enumerate(cursor.fetchall(),1)]
    print('TOP 3 BEST SELLERS:',*lines,sep='\n')

def main():
    conn = connect()
    while True:
        print(  "\n1) List products  2) Search customers  3) Add product\n"+
                "4) Change stock   5) Show receipt      6) Top-3 Best Sellers   0) Quit")
        choice = input("> ")
        if choice == "1":
            list_products(conn)
        elif choice == "2":
            search_customers(conn)
        elif choice == "3":
            add_product(conn)
        elif choice == "4":
            change_stock(conn)
        elif choice == "5":
            get_receipt(conn)
        elif choice == "6":
            best_sellers(conn)
        elif choice == "0":
            break
    conn.close()

main()
