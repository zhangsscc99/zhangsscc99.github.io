def sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    return merge(sort(left), sort(right))

def merge(arr1, arr2):
    res = []
    while arr1 and arr2:
        if arr1[0] <= arr2[0]:
            res.append(arr1.pop(0))
        else:
            res.append(arr2.pop(0))
    res += arr1
    res += arr2
    return res
    




arr1 = [2,3,1,2,5]
arr2 = [12,3123,21,312,321214,28]

print(sort(arr1))
print(sort(arr2))