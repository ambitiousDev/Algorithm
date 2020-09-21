import time


def largestPalindrom(digits):
    min, max, temp, pal = '1', '', 0, 0
    for _ in range(1, digits):
        min += '0'
    for _ in range(0, digits):
        max += '9'

    min = int(min)-1
    max = int(max)
    start = time.time()
    for i in range(max, min, -1):
        for j in range(max, min, -1):
            temp = i*j
            if temp < pal:
                break
            if str(temp) == "".join(reversed(str(temp))):
                pal = temp
    end = time.time()

    print(pal, end=' ')
    print(end-start)


if __name__ == '__main__':
    largestPalindrom(3)
