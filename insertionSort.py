

arr = [4, 3, 1, 8, 11, 5, 16, 9, 0]
n = len(arr)

for i in range(1, n):
    key = arr[i]
    j = i-1
    while j >= 0 and key < arr[j]:
        arr[j+1] = arr[j]
        arr[j] = key
        j -= 1

print(arr)
