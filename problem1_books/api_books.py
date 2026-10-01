import requests

from database import create_database, insert_books, fetch_all_books


API_URL = "https://openlibrary.org/search.json"


def fetch_books(search_query, limit=10):
    """
    Fetch book information from the Open Library API.

    Parameters:
        search_query (str): Search term for books.
        limit (int): Maximum number of books to retrieve.

    Returns:
        list: List of dictionaries containing book information.
    """

    params = {
        "q": search_query,
        "limit": limit
    }

    response = requests.get(
        API_URL,
        params=params,
        timeout=10
    )

    response.raise_for_status()

    data = response.json()

    books = []

    for book in data.get("docs", []):
        title = book.get("title")

        if not title:
            continue

        authors = book.get("author_name", [])

        if authors:
            author = ", ".join(authors)
        else:
            author = "Unknown"

        publication_year = book.get("first_publish_year")

        books.append({
            "title": title,
            "author": author,
            "publication_year": publication_year
        })

    return books


def display_books(books):
    """
    Display books in a readable table format.
    """

    print("\nBooks stored in database")
    print("-" * 100)

    print(
        f"{'ID':<5}"
        f"{'Title':<45}"
        f"{'Author':<35}"
        f"{'Year':<10}"
    )

    print("-" * 100)

    for book in books:
        print(
            f"{book['id']:<5}"
            f"{book['title'][:43]:<45}"
            f"{book['author'][:33]:<35}"
            f"{str(book['publication_year'] or 'Unknown'):<10}"
        )


def main():

    print("=" * 60)
    print("       OPEN LIBRARY BOOK DATA RETRIEVER")
    print("=" * 60)

    search_query = input("\nEnter a book search term: ").strip()

    if not search_query:
        print("Search term cannot be empty.")
        return

    try:
        # Fetch books from Open Library
        print("\nFetching data from Open Library...")

        books = fetch_books(
            search_query,
            limit=10
        )

        if not books:
            print("No books found.")
            return

        print(f"Retrieved {len(books)} books.")

        # Create/connect to SQLite database
        connection = create_database()

        # Insert books into database
        insert_books(
            connection,
            books
        )

        # Retrieve books from database
        stored_books = fetch_all_books(connection)

        # Display retrieved data
        display_books(stored_books)

        connection.close()

        print("\nData successfully stored in books.db")

    except requests.exceptions.RequestException as error:
        print(f"\nAPI request failed: {error}")

    except Exception as error:
        print(f"\nAn unexpected error occurred: {error}")


if __name__ == "__main__":
    main()