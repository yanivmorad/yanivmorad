import time
from concurrent.futures import ThreadPoolExecutor, Future
import requests
from requests import RequestException


# second = 6 #input("")
# while second >= 0.1:
#     time.sleep(0.1)
#     second-=0.1
#     # print((round(second,1)))
#
#     if second % 1 < 0.1:
#         response = requests.get("https://api.kanye.rest")
#         print(response.json()['quote'])

# def count_down(num: int):
#     n = 0
#     counter = 0
#     with ThreadPoolExecutor() as executor:
#         while n <= num:
#             print(f"{(num - n):.1f} seconds left")
#             time.sleep(0.1)
#             n += 0.1
#             counter += 1
#             if counter % 10 == 0:
#                 executor.submit(get_quote)
#     print('Done')
#
#
# def get_quote():
#     response = requests.get('https://api.kanye.rest')
#     if response.status_code < 400:
#         print(response.json()['quote'])
#     raise RequestException()
# count_down(5)
#
# n = 5

from concurrent.futures import ProcessPoolExecutor, Future

def factorial(n):
    result = 1
    for i in range(1,n+1):
         result *=i
    print( result)


if __name__ == '__main__':
    nums = [1550] * 10000
    start = time.perf_counter()
    with ProcessPoolExecutor(max_workers=7)  as executor:
        futures = [executor.submit(factorial, i) for i in nums]
    # for i in nums:
    #     factorial(i)
    print(time.perf_counter()-start)


