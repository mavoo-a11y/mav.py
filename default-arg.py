# def net_price(list_price, discount, tax):
#     return list_price * (1 - discount) * (1 + tax) 

# print(net_price(500,0, 0.5))

import time

def countdown(start, end):
   for x in range(start, end+1):
        print(x)
        time.sleep(1)
   print("Time's up!")

countdown(0, 10)