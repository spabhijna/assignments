import json
import matplotlib.pyplot as plt


DATA_FILE = "student_scores.json"
OUTPUT_FILE = "scores.png"


def load_student_data(file_path):
    """
    Load student score data from a JSON file.

    Parameters:
        file_path (str): Path to the JSON file.

    Returns:
        list: List of dictionaries containing student data.
    """
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data


def validate_student_data(data):
    """
    Validate student score data.

    Parameters:
        data (list): List of student records.

    Returns:
        list: Validated student records.

    Raises:
        ValueError: If data is invalid.
    """
    if not data:
        raise ValueError("Dataset is empty")

    validated = []
    for record in data:
        name = record.get("name")
        score = record.get("score")

        if not name:
            raise ValueError("Missing student name")

        if score is None:
            raise ValueError(f"Missing score for student: {name}")

        if not isinstance(score, (int, float)):
            raise ValueError(f"Invalid score type for {name}: {score}")

        validated.append({"name": name, "score": score})

    return validated


def calculate_average_score(data):
    """
    Calculate the average score from student data.

    Parameters:
        data (list): List of student records.

    Returns:
        float: Average score.
    """
    scores = [record["score"] for record in data]
    return sum(scores) / len(scores)


def create_bar_chart(data, average_score, output_file):
    """
    Create a bar chart of student scores and save it.

    Parameters:
        data (list): List of student records.
        average_score (float): Average score to display.
        output_file (str): Path to save the chart.
    """
    names = [record["name"] for record in data]
    scores = [record["score"] for record in data]

    plt.figure(figsize=(10, 6))
    plt.bar(names, scores, color='steelblue', edgecolor='navy')

    # Add average line
    plt.axhline(
        y=average_score,
        color='red',
        linestyle='--',
        linewidth=2,
        label=f'Average: {average_score:.2f}'
    )

    plt.title('Student Test Scores', fontsize=16, fontweight='bold')
    plt.xlabel('Student Name', fontsize=12)
    plt.ylabel('Score', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.ylim(0, 100)
    plt.legend()
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()

    # Save the chart
    plt.savefig(output_file, dpi=150, bbox_inches='tight')
    plt.close()


def main():
    print("=" * 60)
    print("       STUDENT SCORE ANALYSIS")
    print("=" * 60)

    try:
        # Load data
        print(f"\nLoading data from {DATA_FILE}...")
        raw_data = load_student_data(DATA_FILE)

        # Validate data
        print("Validating data...")
        validated_data = validate_student_data(raw_data)
        print(f"Loaded {len(validated_data)} student records.")

        # Calculate average
        average = calculate_average_score(validated_data)
        print(f"Average score: {average:.2f}")

        # Create chart
        print("Creating bar chart...")
        create_bar_chart(validated_data, average, OUTPUT_FILE)
        print(f"Chart saved to: problem2_student_scores/{OUTPUT_FILE}")

    except FileNotFoundError:
        print(f"Error: Data file '{DATA_FILE}' not found.")
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{DATA_FILE}'.")
    except ValueError as error:
        print(f"Validation error: {error}")
    except Exception as error:
        print(f"An unexpected error occurred: {error}")


if __name__ == "__main__":
    main()
