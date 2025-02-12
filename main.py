from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

# Simulated database (Replace this with an actual database integration)
books_db = {
    1: {"id": 1, "title": "The Pragmatic Programmer", "author": "Andy Hunt & Dave Thomas"},
    2: {"id": 2, "title": "Clean Code", "author": "Robert C. Martin"},
    3: {"id": 3, "title": "Introduction to the Theory of Computation", "author": "Michael Sipser"},
}

app = FastAPI()

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/healthcheck")
async def health_check():
    """Checks if server is active."""
    return {"status": "active"}

@app.get("/api/v1/books/{book_id}")
async def get_book(book_id: int):
    """
    Retrieves a book by its ID.
    Returns 404 if the book is not found.
    """
    book = books_db.get(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book