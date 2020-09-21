def sumSquareDiff(n):
    sum, square = 0, 0
    for i in range(1, n+1):
        sum += i ** 2
        square += i

    square = square ** 2

    print(square-sum)


sumSquareDiff(100)
