from datetime import datetime
arr = [4, 3, 16, 8, 11, 5, 1, 9, 0, 2, -2]
n = len(arr)


for i in range(n):
    a = n-i-1
    for j in range(a):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]


print(arr)
