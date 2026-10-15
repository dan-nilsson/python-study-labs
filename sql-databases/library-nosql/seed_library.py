'''
Library NoSQL Database Seed
'''
from datetime import datetime, timedelta

delta = timedelta(days=14)

books = [
    {'_id': 1,'title': 'The Great Gatsby','author': 'F. Scott Fitzgerald','year': 1925,'genres': [],'available': 10},
    {'_id': 2,'title': 'To Kill a Mockingbird','author': 'Harper Lee','year': 1960,'available': 10},
    {'_id': 3,'title': '1984','author': 'George Orwell','year': 1949,'available': 10},
    {'_id': 4,'title': 'Pride and Prejudice','author': 'Jane Austen','year': 1813,'available': 10},
    {'_id': 5,'title': 'The Catcher in the Rye','author': 'J.D. Salinger','year': 1951,'available': 10},
    {'_id': 6,'title': 'The Hobbit','author': 'J.R.R. Tolkien','year': 1937,'available': 10},
    {'_id': 7,'title': 'Fahrenheit 451','author': 'Ray Bradbury','year': 1953,'available': 10},
    {'_id': 8,'title': 'Jane Eyre','author': 'Charlotte Brontë','year': 1847,'available': 10},
    {'_id': 9,'title': 'Animal Farm','author': 'George Orwell','year': 1945,'available': 10},
    {'_id': 10,'title': 'The Lord of the Rings','author': 'J.R.R. Tolkien','year': 1954,'available': 10},
    {'_id': 11,'title': 'Brave New World','author': 'Aldous Huxley','year': 1932,'available': 10},
    {'_id': 12,'title': 'The Alchemist','author': 'Paulo Coelho','year': 1988,'available': 10},
    {'_id': 13,'title': 'Moby Dick','author': 'Herman Melville','year': 1851,'available': 10},
    {'_id': 14,'title': 'War and Peace','author': 'Leo Tolstoy','year': 1869,'available': 10},
    {'_id': 15,'title': 'The Odyssey','author': 'Homer','year': 700,'available': 10},
    {'_id': 16,'title': 'Crime and Punishment','author': 'Fyodor Dostoevsky','year': 1866,'available': 10},
    {'_id': 17,'title': 'Les Misérables','author': 'Victor Hugo','year': 1862,'available': 10},
    {'_id': 18,'title': 'Dracula','author': 'Bram Stoker','year': 1897,'available': 10},
    {'_id': 19,'title': 'The Shining','author': 'Stephen King','year': 1977,'available': 10},
    {'_id': 20,'title': 'It','author': 'Stephen King','year': 1986,'available': 10}
]

#borrowed from seed_webshop (c) Haitem
members = [
    {'_id': 1, 'first_name': 'Anna', 'last_name': 'Lindqvist', 'email': 'anna.lindqvist@example.com', 'city': 'Uppsala', 'joined': datetime(2024, 3, 14)},
    {'_id': 2, 'first_name': 'Erik', 'last_name': 'Johansson', 'email': 'erik.j@example.com', 'city': 'Stockholm', 'joined': datetime(2023, 11, 2)},
    {'_id': 3, 'first_name': 'Sara', 'last_name': 'Ahmed', 'email': 'sara.ahmed@example.com', 'city': 'Göteborg', 'joined': datetime(2025, 1, 20)},
    {'_id': 4, 'first_name': 'Johan', 'last_name': 'Berg', 'email': 'johan.berg@example.com', 'city': 'Uppsala', 'joined': datetime(2022, 6, 30)},
    {'_id': 5, 'first_name': 'Maria', 'last_name': 'Nilsson', 'email': 'maria.n@example.com', 'city': 'Malmö', 'joined': datetime(2025, 8, 11)},
    {'_id': 6, 'first_name': 'Ali', 'last_name': 'Hassan', 'email': 'ali.hassan@example.com', 'city': 'Stockholm', 'joined': datetime(2024, 9, 5)},
    {'_id': 7, 'first_name': 'Emma', 'last_name': 'Karlsson', 'email': 'emma.k@example.com', 'city': 'Västerås', 'joined': datetime(2023, 2, 17)},
    {'_id': 8, 'first_name': 'Oskar', 'last_name': 'Persson', 'email': 'oskar.p@example.com', 'city': 'Uppsala', 'joined': datetime(2025, 5, 28)},
    {'_id': 9, 'first_name': 'Fatima', 'last_name': 'Yilmaz', 'email': 'fatima.y@example.com', 'city': 'Göteborg', 'joined': datetime(2024, 12, 1)},
    {'_id': 10, 'first_name': 'Lukas', 'last_name': 'Ek', 'email': 'lukas.ek@example.com', 'joined': datetime(2026, 1, 9)}
]

borrowings = [
    {'_id': 1, 'member': 1, 'book': 1, 'borrowed': datetime(2026,3,1), 'return_by': datetime(2026,3,1)+delta, 'returned': None}
]