# Error Handling Checklist (Part A)

## Program 1: `age_calculator.py`
- **Exceptions Caught:** `ValueError` (invalid integer cast), `InvalidAgeError` (custom exception for ages < 0 or > 150).
- **Recovery Action:** The program prints a user-friendly error message, catches the error inside a `while True` loop, and prompts the user to try again, avoiding a crash.
- **User Sees:** "Invalid input! Please enter a valid whole number for your age." or "Error: Age must be between 0 and 150. Received: -5. Please try again."
- **Internal Logging:** Logs `ERROR` level messages to the console with timestamps using the Python `logging` module whenever invalid input is provided.

## Program 2: `inventory_manager.py`
- **Exceptions Caught:** `KeyError` (item not in catalog), `ValueError` (invalid requested quantity), `InsufficientStockError` (custom exception for requesting more than available).
- **Recovery Action:** Program catches the error gracefully, informs the user why their order couldn't be processed, and completes the execution cycle through the `finally` block instead of crashing abruptly.
- **User Sees:** "Sorry, we cannot fulfill your order. Requested 10, but only 5 'laptop's are available." or specific feedback on why the item isn't recognized.
- **Internal Logging:** Logs `ERROR` level messages to a designated file named `inventory_errors.log`, saving the specific exception trace and user input that caused the failure for developer review.

## Program 3: `grade_calculator.py`
- **Exceptions Caught:** `ValueError` (non-numeric or out-of-range grade input), `ZeroDivisionError` (calculating an average for an empty list).
- **Recovery Action:** For input errors, prompts the user to re-enter. For calculation errors (empty list), it catches the division by zero explicitly, prevents a runtime crash, and alerts the user before exiting cleanly.
- **User Sees:** "Error: No grades were entered, so an average cannot be calculated." or "Invalid input: Please enter a valid number between 0 and 100."
- **Internal Logging:** Logs `WARNING` for minor input mistakes and `ERROR` for the logical failure (division by zero) directly to the console.
