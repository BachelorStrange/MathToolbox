def prime(n):
    if n== 0 or n == 1:
        return False
    i=2
    while i*i <= n:
        if n % i == 0:
            return False
        i = i+1
        return True

a = list(filter(prime, range(50)))
print(a)