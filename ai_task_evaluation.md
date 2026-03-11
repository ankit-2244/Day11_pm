# Part D — AI-Augmented Task Evaluation

## 1. Documentation of the Prompt
**Prompt Given:** "Write a Python decorator called `@retry(max_attempts=3, delay=1)` that automatically retries a function if it raises an exception, with exponential backoff."

## 2. AI-Generated Code
The produced python code can be found executing successfully in `ai_retry_decorator.py`.

## 3. Decorator Test Execution
The AI code has been instrumented in `ai_retry_decorator.py` using a mock `simulate_flaky_api_call` function relying on `random.random() < 0.5` to emulate intermittent network failure. It successfully showcases the exponential logic doubling the wait time before throwing the final error if it surpasses 3 failures.

## 4. Critical Evaluation

The AI-generated `@retry` decorator is a functional prototype for handling transient failures via exponential backoff, but lacks the maturity needed for enterprise production systems.

**Positives:** 
It correctly handles `functools.wraps`. This is vital because replacing a function with a decorator usually overwrites metadata (like the original docstrings and function names), which breaks auto-generation tools like Sphinx or logging statements. By using `@functools.wraps(func)`, the metadata is explicitly preserved. 

**Areas for Improvement:**
The most glaring omission is the absence of exception filtering. The current implementation uses a bare `except Exception as e:` which incorrectly treats **every** error as retryable. In a production system, we must distinguish between *retryable exceptions* (e.g., `ConnectionTimeout`, `503 Service Unavailable`) and *non-retryable exceptions* (e.g., `ValueError`, `KeyError`, `401 Unauthorized`). Retrying a syntax error or a bad API key multiple times guarantees continued failure and wastes processing cycles.

**Future Enhancements:**
To improve this, I would modify the decorator signature to accept an `exceptions=(ConnectionError, TimeoutError)` tuple parameter. The `try/except` block should exclusively trap exceptions matching that tuple to trigger the retry, while immediately raising all generic logic violations. Furthermore, adding jitter (randomized variation to the delay) would prevent "thundering herd" problems where multiple retrying clients overwhelm the restored service simultaneously.
