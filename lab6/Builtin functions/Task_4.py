import time
import math

def delayed_sqrt(number, delay_ms):
    time.sleep(delay_ms / 1000)  # Convert milliseconds to seconds
    print(f"Square root of {number} after {delay_ms} milliseconds is {math.sqrt(number)}")

delayed_sqrt(25100, 2123)
