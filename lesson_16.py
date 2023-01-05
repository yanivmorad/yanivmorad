import math
import time
from datetime import datetime
from functools import lru_cache


@lru_cache
def factorial(num):
    return math.factorial(num)
start = datetime.now()
factorial(80000)
factorial(800000)
factorial(800000)
factorial(800000)
factorial(800000)
print(datetime.now()-start)