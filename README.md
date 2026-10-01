# Assignment 1 - Python, API, Data Processing and Database

This project implements Problems 1-3 of Assignment 1, covering API data retrieval, data processing and visualization, and CSV database import.

## Assignment Problem 1 - API Data Retrieval and SQLite

Fetches book data from the Open Library REST API, stores it in a local SQLite database, and displays the retrieved records.

**See:** [problem1_books/README.md](problem1_books/README.md)

## Assignment Problem 2 - Student Score Analysis

Loads student score data, calculates the average score, and creates a bar chart to visualize the data.

**See:** [problem2_student_scores/README.md](problem2_student_scores/README.md)

## Assignment Problem 3 - CSV to SQLite

Reads user data from a CSV file and imports it into a SQLite database with validation and duplicate handling.

**See:** [problem3_csv_database/README.md](problem3_csv_database/README.md)

## Assignment Problem 4 - Most Complex Python Code

**Most Complex Code:** [https://github.com/spabhijna/Football-pipeline/blob/main/src/frame_processor.py](https://github.com/example/complex-python-code)

## Assignment Problem 5 - Most Complex Database Code

**Most Complex Database Code:** [https://github.com/spabhijna/Recomendation-system/blob/main/data/repositories.py](https://github.com/example/complex-database-code)

## Technologies Used

- Python 3
- uv (package management)
- Requests (HTTP requests)
- SQLite (database)
- Matplotlib (data visualization)
- CSV (data import)

## Running the Projects

### Problem 1

```bash
uv run python problem1_books/api_books.py
```

### Problem 2

```bash
uv run python problem2_student_scores/student_scores.py
```

### Problem 3

```bash
uv run python problem3_csv_database/csv_to_database.py
```

# Assignment 2 PDF

**Assignment Document:** [Assignment 2.pdf](Assignment%202.pdf)


## Project Structure

```
assignment/
├── problem1_books/
│   ├── api_books.py
│   ├── database.py
│   └── README.md
├── problem2_student_scores/
│   ├── student_scores.py
│   ├── student_scores.json
│   ├── scores.png
│   └── README.md
├── problem3_csv_database/
│   ├── users.csv
│   ├── csv_to_database.py
│   └── README.md
├── pyproject.toml
├── uv.lock
├── README.md
├── Assignment 2.pdf
└── .gitignore
```
