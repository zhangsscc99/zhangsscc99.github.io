# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     left = arr[:mid]
#     right = arr[mid:]
#     return merge(merge_sort(left), merge_sort(right))

# def merge(left, right):
#     l, r = 0, 0
#     res = []
#     while l < len(left) and r < len(right):
#         if left[l] < right[r]:
#             res.append(left[l])
#             l += 1
#         else:
#             res.append(right[r])
#             r += 1

#     res += left[l:]
#     res += right[r:]
#     return res

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    return merge(merge_sort(left), merge_sort(right))

def merge(left, right):
    l = 0 
    r = 0
    res = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            res.append(left[l])
            l += 1
        else:
            res.append(right[r])
            r += 1
        
    while l < len(left):
        res.append(left[l])
        l += 1
    
    while r < len(right):
        res.append(right[r])
        r += 1
    return res
arr = [33, 55, 12, 1, 5]
print(merge_sort(arr))
