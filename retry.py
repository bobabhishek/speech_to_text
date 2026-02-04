# retry.py
import time


def retry_operation(operation, retries=3, delay=2):
    for attempt in range(retries):
        try:
            return operation()
        except Exception as e:
            print(f"Retry {attempt + 1} failed: {e}")
            time.sleep(delay)

    raise RuntimeError("Azure Speech API failed after retries")
