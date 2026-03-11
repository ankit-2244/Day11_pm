import logging

# Set up logging for grade calculations
logging.basicConfig(level=logging.WARNING, format='%(levelname)s: %(message)s')

def calculate_average_grade():
    """Calculates the average of a list of grades with exception handling."""
    print("--- Grade Calculator ---")
    grades = []
    
    while True:
        try:
            entry = input("Enter a grade (0-100) or 'done' to calculate: ").strip()
            
            if entry.lower() == 'done':
                break
                
            grade = float(entry)
            
            if grade < 0 or grade > 100:
                raise ValueError("Grade must be between 0 and 100.")
                
            grades.append(grade)
            
        except ValueError as ve:
            logging.warning(f"Invalid grade entry: {entry} - {ve}")
            print(f"Invalid input: {ve} Please enter a valid number between 0 and 100.")
    
    print("\n--- Final Calculation ---")
    try:
        # If no grades were entered, this will raise a ZeroDivisionError intentionally
        if not grades:
            raise ZeroDivisionError("Cannot calculate average of an empty grade list.")
            
        avg = sum(grades) / len(grades)
        
    except ZeroDivisionError as zde:
        logging.error(f"Calculation failed: {zde}")
        print("Error: No grades were entered, so an average cannot be calculated.")
    else:
        print(f"You entered {len(grades)} grades.")
        print(f"Your average grade is: {avg:.2f}")
    finally:
        print("Grade calculation process terminated.")

if __name__ == "__main__":
    calculate_average_grade()
