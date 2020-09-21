def is_prime(n):
    nums_to_check = range(2, int(n**.5) + 1)
    for i in nums_to_check:
        if n % i == 0:
            return False
    return True


sum = 0

for i in range(2, 2000000):
    if is_prime(i):
        sum += i


print(sum)
