def minimize_ugliness(n, items, movable):
    # 分离不可移动的物品及其类别
    fixed_items = [(items[i], i) for i in range(n) if movable[i] == 0]
    movable_items = [items[i] for i in range(n) if movable[i] == 1]

    # 按类别分开可移动的物品
    movable_type1 = [item for item in movable_items if item == 1]
    movable_type2 = [item for item in movable_items if item == 2]

    # 按照不可移动物品的位置依次插入可移动物品
    result = []
    j = 0  # movable_items index
    for item, index in fixed_items:
        # 尝试在每个不可移动物品之前插入可移动物品
        while j < len(movable_type1) and (len(result) == 0 or result[-1] == 2):
            result.append(movable_type1.pop(0))  # 插入类别1的物品
        while j < len(movable_type2) and (len(result) == 0 or result[-1] == 1):
            result.append(movable_type2.pop(0))  # 插入类别2的物品
        # 插入当前不可移动物品
        result.append(item)

    # 把剩余的可移动物品插入到最后
    result.extend(movable_type1 + movable_type2)

    # 计算美观不良程度
    ugliness = sum(1 for i in range(1, len(result)) if result[i] != result[i - 1])

    return result, ugliness


# 示例输入
n = 6
items = [1, 2, 1, 2, 1, 2]
movable = [1, 0, 1, 1, 0, 1]

# 调用函数
result, ugliness = minimize_ugliness(n, items, movable)

print(f"最终排列: {result}")
print(f"美观不良程度: {ugliness}")

n = 5
items = [1, 2, 1, 2, 1]
movable = [0, 1, 1, 0, 1]
print(minimize_ugliness(n, items, movable))
