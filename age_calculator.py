import logging

# Configure logging to console
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

class InvalidAgeError(Exception):
    """Custom exception for invalid age ranges."""
    pass

def calculate_future_age():
    """Calculates the user's age in 10 years, with robust error handling."""
    print("--- Age Calculator ---")
    while True:
        try:
            user_input = input("Enter your current age (or type 'quit' to exit): ")
            if user_input.lower() == 'quit':
                break
                
            age = int(user_input)
            
            if age < 0 or age > 150:
                raise InvalidAgeError(f"Age must be between 0 and 150. Received: {age}")
                
        except ValueError as e:
            logging.error(f"User entered non-integer value: {user_input}")
            print("Invalid input! Please enter a valid whole number for your age.")
        except InvalidAgeError as e:
            logging.error(f"Invalid age range error: {e}")
            print(f"Error: {e}. Please try again.")
        else:
            future_age = age + 10
            print(f"Success! In 10 years, you will be {future_age} years old.")
            break
        finally:
            print("-> Input processing cycle completed.\n")
            
if __name__ == "__main__":
    calculate_future_age()
