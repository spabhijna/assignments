# Problem 3 - CSV to SQLite

## Objective

Read user data from a CSV file and import it into a SQLite database with validation and duplicate handling.

## CSV Structure

The CSV file (`users.csv`) has the following format:

```csv
name,email
Alice Johnson,alice@example.com
Bob Smith,bob@example.com
```

- **name**: User's full name (required, cannot be empty)
- **email**: User's email address (required, cannot be empty, must be unique)

## Database Schema

```sql
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
);
```

Database file: `users.db`

The `email` field has a `UNIQUE` constraint to prevent duplicate email addresses.

## Import Process

1. **Read CSV**: The CSV file is read using Python's built-in `csv` module
2. **Validate Records**: Each record is validated to ensure:
   - Name is not empty
   - Email is not empty
3. **Insert Records**: Valid records are inserted into the database using parameterized SQL queries
4. **Handle Duplicates**: Duplicate email addresses are caught by the `UNIQUE` constraint and skipped gracefully
5. **Query Database**: All stored users are retrieved and displayed

## Validation

The following validation rules are applied:

- **Name**: Cannot be empty or whitespace-only
- **Email**: Cannot be empty or whitespace-only

Invalid records are skipped with a descriptive message.

## Duplicate Handling

Duplicate email addresses are handled using SQLite's `UNIQUE` constraint:

- When a duplicate email is encountered, an `IntegrityError` is raised
- The error is caught and the duplicate record is skipped
- A message is printed indicating which email was skipped
- The import process continues for remaining records

## How to Run

```bash
uv run python problem3_csv_database/csv_to_database.py
```

## Example Output

```
============================================================
       CSV TO SQLITE IMPORTER
============================================================

Reading users.csv...
Inserted 5 users.

Users stored in database:
------------------------------------------------------------
ID    Name                    Email                         
------------------------------------------------------------
1     Alice Johnson           alice@example.com             
2     Bob Smith               bob@example.com               
3     Charlie Brown           charlie@example.com           
4     David Wilson            david@example.com             
5     Emma Davis              emma@example.com               

Data successfully stored in users.db
```

If there are duplicates or invalid records:

```
Reading users.csv...
Skipping duplicate email: alice@example.com
Inserted 4 users.
Skipped 1 records (invalid or duplicates).
```

## Error Handling

The program handles:

- **Missing CSV file**: `FileNotFoundError` if the CSV file doesn't exist
- **Invalid records**: Skipped with descriptive error messages
- **Duplicate emails**: Caught by `sqlite3.IntegrityError` and skipped
- **CSV parsing errors**: Handled by the csv module
- **Database errors**: Caught by general exception handler
