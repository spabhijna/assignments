import csv
import sqlite3


CSV_FILE = "users.csv"
DATABASE_NAME = "users.db"


def create_database():
    """
    Create the SQLite database and users table
    if they do not already exist.
    """
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
    """)

    connection.commit()
    return connection


def read_csv_file(file_path):
    """
    Read user data from a CSV file.

    Parameters:
        file_path (str): Path to the CSV file.

    Returns:
        list: List of dictionaries containing user data.
    """
    users = []
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            users.append({
                'name': row.get('name', '').strip(),
                'email': row.get('email', '').strip()
            })
    return users


def validate_user(user):
    """
    Validate a user record.

    Parameters:
        user (dict): User record with name and email.

    Returns:
        tuple: (is_valid, error_message)
    """
    if not user['name']:
        return False, "Name cannot be empty"

    if not user['email']:
        return False, "Email cannot be empty"

    return True, None


def insert_users(connection, users):
    """
    Insert valid users into the SQLite database.

    Handles duplicate emails gracefully.

    Parameters:
        connection: SQLite database connection.
        users (list): List of user records.

    Returns:
        tuple: (inserted_count, skipped_count)
    """
    cursor = connection.cursor()
    inserted = 0
    skipped = 0

    for user in users:
        is_valid, error = validate_user(user)

        if not is_valid:
            print(f"Skipping invalid record: {error}")
            skipped += 1
            continue

        try:
            cursor.execute("""
                INSERT INTO users (name, email)
                VALUES (?, ?)
            """, (user['name'], user['email']))
            connection.commit()
            inserted += 1

        except sqlite3.IntegrityError:
            print(f"Skipping duplicate email: {user['email']}")
            skipped += 1

    return inserted, skipped


def fetch_all_users(connection):
    """
    Retrieve all users stored in the database.

    Parameters:
        connection: SQLite database connection.

    Returns:
        list: Users represented as dictionaries.
    """
    cursor = connection.cursor()
    cursor.execute("""
        SELECT id, name, email
        FROM users
        ORDER BY id
    """)

    rows = cursor.fetchall()

    users = []
    for row in rows:
        users.append({
            'id': row[0],
            'name': row[1],
            'email': row[2]
        })

    return users


def display_users(users):
    """
    Display users in a readable table format.
    """
    print("\nUsers stored in database:")
    print("-" * 60)
    print(f"{'ID':<5}{'Name':<25}{'Email':<30}")
    print("-" * 60)

    for user in users:
        print(f"{user['id']:<5}{user['name'][:23]:<25}{user['email'][:28]:<30}")


def main():
    print("=" * 60)
    print("       CSV TO SQLITE IMPORTER")
    print("=" * 60)

    try:
        # Read CSV file
        print(f"\nReading {CSV_FILE}...")
        users = read_csv_file(CSV_FILE)

        if not users:
            print("No users found in CSV file.")
            return

        # Create/connect to database
        connection = create_database()

        # Insert users
        inserted, skipped = insert_users(connection, users)
        print(f"Inserted {inserted} users.")
        if skipped > 0:
            print(f"Skipped {skipped} records (invalid or duplicates).")

        # Retrieve and display users
        stored_users = fetch_all_users(connection)
        display_users(stored_users)

        connection.close()

        print(f"\nData successfully stored in {DATABASE_NAME}")

    except FileNotFoundError:
        print(f"Error: CSV file '{CSV_FILE}' not found.")
    except Exception as error:
        print(f"An unexpected error occurred: {error}")


if __name__ == "__main__":
    main()
