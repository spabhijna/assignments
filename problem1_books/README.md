# Problem 1 - API Data Retrieval and SQLite

## Objective

Fetch book data from the Open Library REST API, store it in a local SQLite database, and display the retrieved records.

## API Used

**Open Library REST API**

- API Endpoint: `https://openlibrary.org/search.json`
- Example: `https://openlibrary.org/search.json?q=python&limit=10`

## Data Fields Extracted

- **title**: Book title (required)
- **author**: Author name(s) - defaults to "Unknown" if missing
- **publication_year**: First publication year - NULL if missing

## SQLite Schema

```sql
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT,
    publication_year INTEGER
);
```

Database file: `books.db`

## Program Flow

```
Open Library API
       ↓
   HTTP Request
       ↓
    JSON Data
       ↓
 Data Processing
       ↓
     SQLite
       ↓
   SQL Query
       ↓
    Display
```

### Functions

- `fetch_books()`: Fetches data from Open Library API
- `create_database()`: Creates SQLite database and table
- `insert_books()`: Inserts book records into database (clears existing records first)
- `fetch_all_books()`: Retrieves all books from database
- `display_books()`: Displays books in a readable table format
- `main()`: Orchestrates the entire workflow

## How to Run

```bash
uv run python problem1_books/api_books.py
```

## Example Output

```
============================================================
       OPEN LIBRARY BOOK DATA RETRIEVER
============================================================

Enter a book search term: python

Fetching data from Open Library...
Retrieved 10 books.

Books stored in database
----------------------------------------------------------------------------------------------------
ID    Title                                        Author                              Year    
----------------------------------------------------------------------------------------------------
1     Python Crash Course                          Eric Matthes                        2015    
2     Learning Python                              Mark Lutz                           1999    
3     Python Programming                           John M. Zelle                       2010    
...

Data successfully stored in books.db
```

## Error Handling

The program handles:

- **Empty search input**: Prompts user to enter a valid search term
- **API/network errors**: Catches `requests.exceptions.RequestException`
- **HTTP errors**: Uses `response.raise_for_status()`
- **Invalid/unexpected API response**: Gracefully handles missing fields
- **Missing book fields**: 
  - Missing author → "Unknown"
  - Missing publication year → NULL
- **SQLite errors**: Caught by general exception handler

## Important Implementation Decisions

1. **Parameterized SQL queries**: All SQL queries use parameterized statements (`?` placeholders) to prevent SQL injection
2. **Clear existing records**: Before inserting new search results, the table is cleared to avoid duplicates
3. **Separate database module**: SQLite-specific operations are isolated in `database.py` for better separation of concerns
4. **Graceful field handling**: Missing fields are handled with defaults rather than causing errors
5. **Connection management**: Database connection is explicitly closed after operations
