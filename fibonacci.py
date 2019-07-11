# Fibonacci sequence using memoization 

'''
Declare python dict, which works as a cache for storing and searching the fibonacci calculations
'''
fibonacci_cache = {}
def fibonacci (num):

    if type(num) != int:
        return False
    if num in fibonacci_cache:
        return fibonacci_cache[num]
    if num == 0:
        return 1
    elif num == 1:
        return 1
    else:
        value = fibonacci(num-1) + fibonacci(num-2)
        fibonacci_cache[num] = value
        return value

'''
Now, print first 1000th fibonacci numbers and see how your system behaves
'''
for num in range (0,1000):
    print num , ":", fibonacci(num)
