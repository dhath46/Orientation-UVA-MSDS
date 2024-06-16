def prime_ftr(n):
    ftr = 2
    while ftr * ftr <= n:
        if n % ftr:
            ftr += 1
        else:
            n //= ftr
    return n

num = 600851475143
result = prime_ftr(num)
print(result)
