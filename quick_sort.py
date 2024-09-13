def partition(arr, low , high):
    j = low 
    pivot = arr[low]
    for i in range(low + 1, high + 1):
        if arr[i] <= pivot:
            j += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[j], arr[low] = arr[low], arr[j]
    return j

def quick_sort_between(arr, low, high):
    if high - low <= 0:
        return 
    m = partition(arr, low, high)
    quick_sort_between(arr, low, m - 1)
    quick_sort_between(arr, m + 1, high)

def quick_sort(arr):
    quick_sort_between(arr, 0, len(arr) - 1)


array = [3, 2, 1, 5, 99, 25]
quick_sort(array)
print(array)