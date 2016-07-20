import math

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
    return sum([i*i for i in range(n)[1::n])

if __name__ == "__main__":
    print(sum_squares_modified(4))