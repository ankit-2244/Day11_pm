import json
import logging

logging.basicConfig(
    filename='app_processing.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# --- Q2: Coding ---

def safe_json_load(filepath):
    """
    Safely reads a JSON file and handles potential exceptions.
    Returns:
        The parsed dictionary on success.
        None on failure.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
    except FileNotFoundError as e:
        logging.error(f"File not found: {filepath}. Exception: {e}")
        return None
    except json.JSONDecodeError as e:
        logging.error(f"Failed to decode JSON from {filepath}. Exception: {e}")
        return None
    except PermissionError as e:
        logging.error(f"Permission denied for {filepath}. Exception: {e}")
        return None
    except Exception as e:
        logging.error(f"An unexpected error occurred reading {filepath}. Exception: {e}")
        return None

# --- Q3: Debug / Analyze ---

# BUGGY CODE PROVIDED:
# def process_data(data_list):
#     results = []
#     for item in data_list:
#         try:
#             value = int(item)
#             results.append(value * 2)
#         except:
#             print("Error occurred")
#             continue
#         finally:
#             return results
#     return results

# ISSUES FIXED:
# 1. Bare `except:` replaced with `except ValueError as e:` to catch only the expected integer casting errors.
# 2. `return results` removed from `finally:`. Placing return in finally forces the loop to exit on the very first iteration, overriding the loop flow.
# 3. Added specific details to the error message inside the `except` block so it's informative. `continue` was removed because it's the natural behavior of the loop anyway if we don't return.

def process_data_fixed(data_list):
    """
    Processes a list of potential integer strings and doubles them safely.
    Handles ValueError specifically, without breaking loop logic.
    """
    results = []
    for item in data_list:
        try:
            value = int(item)
            results.append(value * 2)
        except ValueError as e:
            # Informative error message instead of generic "Error occurred"
            print(f"Failed to process '{item}': Not a valid integer. ({e})")
            # We don't need 'continue' here, loop naturally advances to next iteration
        except TypeError as e:
             print(f"Failed to process '{item}': Incorrect type received. ({e})")
        # Removing `finally: return results` which caused immediate termination.
    return results

if __name__ == "__main__":
    # Test Q3 Fixed code
    print("Testing process_data_fixed:")
    test_data = ["10", "20", "invalid", "30", None, "40"]
    final_output = process_data_fixed(test_data)
    print(f"Final valid results: {final_output}")
