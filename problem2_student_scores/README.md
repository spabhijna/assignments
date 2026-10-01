# Problem 2 - Student Score Analysis

## Objective

Fetch student score data, calculate the average score, and create a bar chart to visualize the data.

## Data Source

**Local JSON Dataset**

A local JSON file (`student_scores.json`) is used because no suitable publicly accessible API containing student/test-score data was available.

## Data Source Selection

After researching available public APIs, no reliable, free-to-access API was found that provides student test score data in the required format. Therefore, a local JSON dataset was created to demonstrate the data processing and visualization pipeline while maintaining the same structure that would be used with an API response.

## Data Format

```json
[
    {
        "name": "Alice",
        "score": 85
    },
    {
        "name": "Bob",
        "score": 92
    }
]
```

Each record contains:
- **name**: Student name (string, required)
- **score**: Test score (integer or float, required)

## Data Processing

1. **Loading**: Data is loaded from `student_scores.json` using Python's `json` module
2. **Validation**: Each record is validated to ensure:
   - Name is present and not empty
   - Score is present
   - Score is a valid number (int or float)
3. **Average Calculation**: The average is computed programmatically from all valid scores

## Average Calculation

```python
average = sum(scores) / len(scores)
```

The average is calculated dynamically from the loaded data, not hard-coded.

## Visualization

A bar chart is created using `matplotlib` with the following features:
- Student names on X-axis
- Scores on Y-axis (0-100 scale)
- Clear title: "Student Test Scores"
- Readable axis labels
- Rotated X-axis labels for better readability
- Red dashed line indicating the average score
- Grid lines on Y-axis for easier reading
- Saved as `scores.png` at 150 DPI

## How to Run

```bash
uv run python problem2_student_scores/student_scores.py
```

## Example Output

```
============================================================
       STUDENT SCORE ANALYSIS
============================================================

Loading data from student_scores.json...
Validating data...
Loaded 8 student records.
Average score: 85.75
Creating bar chart...
Chart saved to: problem2_student_scores/scores.png
```

## Error Handling

The program handles:
- **Missing data file**: `FileNotFoundError` if JSON file doesn't exist
- **Invalid JSON**: `json.JSONDecodeError` for malformed JSON
- **Empty dataset**: `ValueError` if no records are present
- **Missing student names**: `ValueError` with descriptive message
- **Missing scores**: `ValueError` indicating which student is affected
- **Invalid score types**: `ValueError` for non-numeric scores
- **Unexpected errors**: General exception handler as fallback

## Limitations

- Uses a local dataset instead of a public API (no suitable student-score API was available)
- The dataset is static and would need to be updated manually to reflect new data
