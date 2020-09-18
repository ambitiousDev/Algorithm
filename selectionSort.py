

arr = [4, 3, 1, 8, 11, 5, 16, 9, 0]


for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]


print(arr)
