import random

def partition(arr, low , high):
    j = low 
    pivot = arr[low]
    for i in range(low + 1, high + 1):
        if arr[i] <= pivot:
            j += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[j], arr[low] = arr[low], arr[j]
    return j


# 71 92 38 52


def randomized_partition(arr, low, high):
    # 随机选择一个索引，交换到第一个元素
    rand_index = random.randint(low, high)
    arr[low], arr[rand_index] = arr[rand_index], arr[low]
    return partition(arr, low, high)


def quick_sort_between(arr, low, high):
    if high - low <= 0:
        return 
    m = randomized_partition(arr, low, high)
    quick_sort_between(arr, low, m - 1)
    quick_sort_between(arr, m + 1, high)

def quick_sort(arr):
    quick_sort_between(arr, 0, len(arr) - 1)


array = [3, 2, 1, 5, 99, 25]
quick_sort(array)
print(array)


def randomized_partition(arr, low, high):
    rand_index = random.randint(low, high)
    arr[low], arr[rand_index] = arr[rand_index], arr[low]
    return partition(arr, low, high)

def partition(arr, low, high):
    j = low 
    pivot = arr[low]
    for i in range(low + 1, high + 1):
        if arr[i] < pivot:
            j += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[j], arr[low] = arr[low], arr[j]
    return j

def quick_sort_between(arr, low, high):
    if high - low <= 0:
        return 
    m = randomized_partition(arr, low, high)
    quick_sort_between(arr, low, m - 1)
    quick_sort_between(arr, m + 1, high)

def quick_sort(arr):
    quick_sort_between(arr, 0, len(arr) - 1)


arr = [101, 87, 983, 5, 10]
quick_sort(arr)
print(arr)


def randmized_partition(arr, low, high):
    rand_index = random.randint(low, high)
    arr[rand_index], arr[low] = arr[low], arr[rand_index]
    return partition(arr, low, high)

def partition(arr, low, high):
    pivot = arr[low]
    j = low 
    for i in range(low + 1, high + 1):
        if arr[i] <= pivot:
            j += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[j], arr[low] = arr[low], arr[j]
    return j

def quick_sort_between(arr, low, high):
    if high - low <= 0:
        return 
    m = randomized_partition(arr, low, high)
    quick_sort_between(arr, low, m - 1)
    quick_sort_between(arr, m + 1, high)

def quick_sort(arr):
    quick_sort_between(arr, 0, len(arr) - 1)

arr2 = [91, 72, 38, 52, 100, 110, 150, 192]

quick_sort(arr2)
print(arr2)

# 71 92 38 52
# 71 38 92 52
# 71 38 52 92