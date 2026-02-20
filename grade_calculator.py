def calculate_grade(marks):
    """
    Function to calculate grade and message based on marks
    """
    if 90 <= marks <= 100:
        return "A", "Excellent Work! Keep shining! 🌟"
    elif 80 <= marks <= 89:
        return "B", "Very Good! Keep it up! 👍"
    elif 70 <= marks <= 79:
        return "C", "Good Job! You can do even better! 😊"
    elif 60 <= marks <= 69:
        return "D", "Keep Trying! Practice more! 💪"
    else:
        return "F", "Don’t give up! Work harder and try again! 📚"


def get_valid_marks():
    """
    Function to validate marks input (0-100 only)
    Uses while loop for invalid input handling
    """
    while True:
        try:
            marks = int(input("Enter marks (0-100): "))
            
            if 0 <= marks <= 100:
                return marks
            else:
                print("❌ Invalid input! Marks must be between 0 and 100.")
        
        except ValueError:
            print("❌ Invalid input! Please enter a number.")


def main():
    print("📊 STUDENT GRADE CALCULATOR")
    print("-" * 30)

    name = input("Enter student name: ").strip()
    marks = get_valid_marks()

    grade, message = calculate_grade(marks)

    print("\n📊 RESULT FOR", name.upper() + ":")
    print(f"Marks: {marks}/100")
    print(f"Grade: {grade}")
    print(f"Message: {message}")


if __name__ == "__main__":
    main()