def isprime(n):
    if n >= 1:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    else:
        return False

print(isprime(29))