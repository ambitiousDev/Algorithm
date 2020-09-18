def heapify(arr, n, i):
    biggest = i
    l = 2*i+1
    r = 2*i+2

    if l < n and arr[biggest] < arr[l]:
        biggest = l
    if r < n and arr[biggest] < arr[r]:
        biggest = r

    if biggest != i:
        arr[i], arr[biggest] = arr[biggest], arr[i]
        heapify(arr, n, biggest)


def heapSort(arr):
    n = len(arr)

    for i in range(n):
        heapify(arr, n, i)
    print(arr)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


arr = [12, 11, 13, 5, 6, 7]
heapSort(arr)
print(arr)


array, list, stack, queue, tree, graph


array, list, stack, queue, tree, graph

array, list, stack, queue, tree, graph


selection sort = n2 n2 n2
bubble  n n2 n2
insetion n n2 n2
merge nlogn nlogn nlogn
heap nlogn nlogn nlogn
quick nlogn nlogn n2



cong viec hang ngay nhu the nao, se lam viec voi ai nhieu nhat
dieu anh thich nhat khi lam viec o cong ty la
trang phuc khi di lam 
co tan tam voi intern k 
luc a doc resume cua e thi a thay nhu the nao a
co co hoi trau doi tieng nhat k 
van hoa cua cong ty



