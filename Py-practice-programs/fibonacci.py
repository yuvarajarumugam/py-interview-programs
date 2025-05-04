import sys
sys.set_int_max_str_digits(100000)

# 0 1 1 2 3 5
def fibonacci(n):
    if n < 1:
        print("n should be > 0")
        return

    prev2 = 0
    prev1 = 1

    print(prev2, end=' ')

    if n == 1:
        return

    print(prev1, end=' ')

    for i in range(3, n+1):
        curr = prev2 + prev1
        prev2 = prev1
        prev1 = curr
        print(curr, end=' ')

    print("\n")

if __name__ == '__main__':
    fibonacci(2)


# Method 2:

def fibonacci1(n):
    if n == 0:
        return "N should be > 0"
    elif n == 1:
        return [0]
    else:
        fib_series = [0, 1]

    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series

print(fibonacci1(5))





