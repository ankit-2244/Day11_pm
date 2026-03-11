# Part C - Interview Documentation

## Q1 - Conceptual: complete execution flow of try/except/else/finally

**Execution Flow Overview:**
The `try...except...else...finally` structure in Python allows for granular control over code that might fail. 

1. **`try` block:** Executes first. This is where you place the "risky" code that might raise an exception.
2. **`except` block:** Executes *only* if an exception matching the specified type is raised inside the `try` block. If no exception occurs, this block is skipped entirely. 
3. **`else` block:** Executes *only* if the `try` block succeeds without raising any exceptions at all. It is placed after the `except` blocks but generally houses code that depends on the `try` block succeeding, separating it from the "risky" code. This prevents accidental catching of exceptions that might be raised by code that shouldn't have been in the `try` block to begin with.
4. **`finally` block:** Always executes, unconditionally, at the very end of the try/except/else structure. It runs whether an exception was raised, caught, unhandled, or if everything was perfectly successful. It even executes if there's a `return` or `break` statement inside any of the preceding blocks. It is primarily used for clean-up tasks (like closing files or network connections).

**Exception Inside the `else` Block:**
If an exception occurs inside the `else` block, the exception is *not* caught by the preceding `except` blocks. Python will immediately jump out of the `else` block, execute the `finally` block (if present) for cleanup, and then the exception will be propagated upwards, potentially crashing the program unless caught by a higher-level try-except statement.

**Code Example:**
```python
def division_process(a, b):
    print("Starting process...")
    try:
        result = a / b  # Risky operation
    except ZeroDivisionError as e:
        print(f"Failed! Division by zero isn't allowed: {e}")
    else:
        # Executes only if no ZeroDivisionError occurs
        print(f"Success! Result is {result}")
        
        # If an exception happens here, it is NOT caught by the above except block!
        # For example, if we do: `10 / "apple"` it would crash here.
    finally:
        print("Finishing process. Releasing resources.\n")

# Scenario 1: Succeeds
division_process(10, 2) 

# Scenario 2: ZeroDivisionError
division_process(10, 0)
```
