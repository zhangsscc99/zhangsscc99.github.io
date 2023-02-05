# counting_sort 代码实现

from typing import List
    
def counting_sort(arr:List[int]):
    max=min=0
    for i in arr:
        if i < min:
            min = i
        if i > max:
            max = i 
    count = [0] * (max - min +1)
    #for j in range(max-min+1):
    #    count[j]=0
    for index in arr:
        count[index-min]+=1
    index=0
    for a in range(max-min+1):
        for c in range(count[a]):
            arr[index]=a+min
            index+=1

# 测试数据

if __name__ == '__main__':
    import random
    random.seed(54)
    arr = [random.randint(0,100) for _ in range(10)]
    print("原始数据：", arr)
    counting_sort(arr)
    print("计数排序结果", arr)