# n = 153
def amstrong(n):
    result = n
    length = len(str(n))

    total = 0
    while n > 0:
        digit = n % 10
        total = total + (digit ** length)
        n //= 10
    return total == result

print(amstrong(153))
