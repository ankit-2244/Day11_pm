import time
import random
import functools
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# AI Generated Code based on prompt
def retry(max_attempts=3, delay=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            current_delay = delay
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    logging.warning(f"Attempt {attempts} failed with error: {e}")
                    if attempts >= max_attempts:
                        logging.error(f"Max retries ({max_attempts}) reached. Raising exception.")
                        raise
                    
                    logging.info(f"Retrying in {current_delay} seconds...")
                    time.sleep(current_delay)
                    current_delay *= 2 # Exponential backoff logic
        return wrapper
    return decorator

@retry(max_attempts=3, delay=1)
def simulate_flaky_api_call():
    """
    Simulates a function that fails roughly 50% of the time.
    """
    chance = random.random()
    if chance < 0.5:
        raise ConnectionError(f"Simulated network drop. (Random value: {chance:.2f})")
    return f"Success! Data fetched at {chance:.2f}"

if __name__ == "__main__":
    print("--- Testing the @retry Decorator ---")
    for i in range(3): # Run 3 separate test cycles
        print(f"\nTest Cycle {i+1}:")
        try:
            result = simulate_flaky_api_call()
            print(f"Final Outcome: {result}")
        except ConnectionError as e:
            print(f"Final Outcome: Function ultimately failed. Error: {e}")
