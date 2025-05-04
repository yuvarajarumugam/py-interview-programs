def factorial_number(n):
    if n == 0:
        return 1

    if n < 1:
        return

    if n > 1:
        factorial = 1
        for i in range(n, 0, -1):
            factorial *= i

        return factorial

print(factorial_number(10))