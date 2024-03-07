def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))

def merge(left, right):
    res = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))
    res += left
    res += right
    return res
    

arr1 = [12321, 12312 ,12, 1, 1,21,321,321,3,123,213,21]
arr2 = [10, 1, 3,5,6,56,54,654]
print(merge_sort(arr1))
print(merge_sort(arr2))