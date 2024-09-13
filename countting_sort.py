# quick_sort 代码实现

def partition(arr, low: int, high: int):
    pivot, j = arr[low], low
    for i in range(low + 1, high + 1):
        if arr[i] <= pivot:
            j += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[low], arr[j] = arr[j], arr[low]
    return j 
    #71 38 52 92 
def partition(arr, low, high):
    pivot, j = arr[low], low 
    for i in range(low + 1, high + 1):
        if arr[i] <= pivot:
            j += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[low], arr[j] = arr[j], arr[low]
    return j

def partition(arr, low, high):
    pivot = arr[low]
    j = low
    for i in range(low + 1, high + 1):
        if arr[i] <= pivot:
            j += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[low], arr[j] = arr[j], arr[low]
    return j

def quick_sort_between(arr, low: int, high: int):
    if high-low <= 1: # 递归结束条件
        return

    m = partition(arr, low, high)  # arr[m] 作为划分标准
    quick_sort_between(arr, low, m - 1)
    quick_sort_between(arr, m + 1, high)

def quick_sort(arr):
    """
    快速排序(in-place)
    :param arr: 待排序的List
    :return: 快速排序是就地排序(in-place)
    """
    quick_sort_between(arr,0, len(arr) - 1)


# 测试数据

if __name__ == '__main__':
    import random
    random.seed(54)
    arr = [random.randint(0,100) for _ in range(10)]
    print("原始数据：", arr)
    quick_sort(arr)
    print("快速排序结果：", arr)


def partition(arr, low, high):
    j = low
    pivot = arr[low]
    for i in range(low + 1, high + 1):
        if arr[i] <= pivot:
            j += 1
            arr[i], arr[j] = arr[j], arr[i]
        
    arr[j], arr[low] = arr[low], arr[j]

def quick_sort_between(arr, low, high):
    if high - low <= 1:
        return 
    m = partition(arr, low, high)
    quick_sort_between(arr, low, m - 1)
    quick_sort_between(arr, m + 1, high)

def quick_sort(arr):
    quick_sort_between(arr, 0, len(arr) - 1)

