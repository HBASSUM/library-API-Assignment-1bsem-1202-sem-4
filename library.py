import asyncio
from typing import List, Dict

# Fake data
books: List[Dict] = [
    {"id": 1, "title": "Python", "available": True},
    {"id": 2, "title": "Data Science", "available": True}
]

# Endpoint 1: GET /books
async def get_books() -> List[Dict]:
    await asyncio.sleep(1)
    return books

# Endpoint 2: POST /borrow
async def borrow_book(user_id: int, book_id: int) -> str:
    await asyncio.sleep(1)

    for book in books:
        if book["id"] == book_id and book["available"]:
            book["available"] = False
            return f"User {user_id} borrowed book {book_id}"

    return "Book not available"

# Simulate multiple users
async def main():
    print(await get_books())

    results = await asyncio.gather(
        borrow_book(1, 1),
        borrow_book(2, 2)
    )

    for r in results:
        print(r)

# Run
asyncio.run(main())
