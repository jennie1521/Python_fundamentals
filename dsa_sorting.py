#bubble sort
arr=[7,3,4,2,8,1,9]
n=len(arr)
for i in range (n):
    for j in range(n-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr)

#insertion sort
arr=[10,4,2,8,3,9,5]
for i in range(1,len(arr)):
    key=arr[i]
    j=i-1
    while j>=0 and arr[j]>arr[j+1]:
        arr[j+1]=arr[j]
        j-=1
        arr[j+1]=key
print(arr)

#selection sort
arr=[37,12,98,56,73]
n=len(arr)
for i in range(n):
    min_index=i
    for j in range(i+1,n):
        if arr[j]<arr[min_index]:
            min_index=j
    arr[i],arr[min_index]=arr[min_index],arr[i]
print(arr) 

#merge sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    l_half = arr[:mid]
    r_half = arr[mid:]

    l_half = merge_sort(l_half)
    r_half = merge_sort(r_half)

    return merge(l_half, r_half)

def merge(left, right):
    new = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            new.append(left[i])
            i += 1
        else:
            new.append(right[j])
            j += 1

    new.extend(left[i:])
    new.extend(right[j:])
    return new

arr = [43, 88, 57, 19, 5, 62, 68, 35]
print(merge_sort(arr))

#quick sort
def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot-1)
        quick_sort(arr, pivot+1, high)

def partition(arr, low, high):
    p = arr[low]
    i = low + 1
    j = high

    while True:
        while i <= j and arr[i] <= p:
            i += 1
        while i <= j and arr[j] >= p:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break

    arr[low], arr[j] = arr[j], arr[low]
    return j

arr = [5,8,1,2,6,3,9]
quick_sort(arr, 0, len(arr)-1)
print(arr)
