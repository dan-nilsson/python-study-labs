# Library NoSQL Lab

## Database Schema
- members: _id: int, first_name: str, last_name: str, email: str (unique), city: srt, joined: datetime
- books: _id: int, title: str, author: str, year: int, genres: list, available: int
- reviews: _id: int, member: int, rating: int
- borrowings: _id: int, member: int, book: int, borrowed: datetime, returned: datetime