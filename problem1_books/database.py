import sqlite3


DATABASE_NAME = "books.db"


def create_database():
    """
    Create the SQLite database and books table
    if they do not already exist.
    """

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT,
            publication_year INTEGER
        )
    """)

    connection.commit()

    return connection


def insert_books(connection, books):
    """
    Insert books into the SQLite database.

    Existing records are cleared before inserting
    the latest API results.
    """

    cursor = connection.cursor()

    # Clear previous results
    cursor.execute("DELETE FROM books")

    query = """
        INSERT INTO books (
            title,
            author,
            publication_year
        )
        VALUES (?, ?, ?)
    """

    book_data = [
        (
            book["title"],
            book["author"],
            book["publication_year"]
        )
        for book in books
    ]

    cursor.executemany(
        query,
        book_data
    )

    connection.commit()


def fetch_all_books(connection):
    """
    Retrieve all books stored in the database.

    Returns:
        list: Books represented as dictionaries.
    """

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            id,
            title,
            author,
            publication_year
        FROM books
        ORDER BY id
    """)

    rows = cursor.fetchall()

    books = []

    for row in rows:
        books.append({
            "id": row[0],
            "title": row[1],
            "author": row[2],
            "publication_year": row[3]
        })

    return books


def close_database(connection):
    """
    Close the database connection.
    """

    if connection:
        connection.close()