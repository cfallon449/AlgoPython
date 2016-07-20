import math
import random

# R-1.1
def is_multiple(n,m):
    return n % m == 0


# R-1.2
def is_even(k):
    if isinstance(k, int):
        return k % 2 == 0
    else:
        return False


# R-1.3
def minmax(data):
    sorted_data = sorted(data)
    return data[0], data[-1]


# R-1.4
def sum_squares(n):
    if isinstance(n, int) & n > 0:
        sum_squares = 0
        while n > 0:
            n -= 1
            sum_squares += n*n
        return sum_squares
    else:
        return 0


# R-1.5
def sum_squares_modified(n):
    return sum([i*i for i in range(n-1)])


# R-1.6 & R-1.7
def sum_odd_squares(n):
    return sum([i*i for i in range(0,n,2)])


# R-1.9
def range_1():
    return [i for i in range(50,90,10)]


# R-1.10
def range_2():
    return [i for i in range(8,-10,-2)]


# R-1.11
def list_comprehension():
    return [math.pow(2,i) for i in range(0,9,1)]


# R-1.12
def choice(data):
    return data[random.randrange(0,len(data))]


# C-1.13
def reverse_order(data):
    return [i for i in data[::-1]]


# C-1.14
def odd_product(data):
    return set((i,j) for i,j in ((i,j) for i in data for j in data) if i*j % 2 != 0).__len__() != 0


# C-1.15
def distinct_numbers(data):
    return set(data).__len__() == data.__len__()


# C-1.18
def list_comprehension_2():
    return [sum(range(0,20,2)[:x])+x for x in range(0,20,2)]

# C-1.19
def characters_comprehension():
    return [chr(i).lower() for i in range(65,91)]


# C-1.28
def norm(v,p):
    return math.pow(sum(map(lambda x: math.pow(x,p), v)),1/p)


# C-1.35
def birthday_paradox(n):
    birthdays = [random.randrange(1,365) for i in range(1,n)]
    return set(birthdays).__len__() != birthdays.__len__()

if __name__ == "__main__":
    print(list(map(lambda x: birthday_paradox(x), range(5,100,5))))
