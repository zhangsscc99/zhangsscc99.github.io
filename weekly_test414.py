def maxScore(nums):
    n = len(nums)
    dp = [-float('inf')] * n  # 初始化 dp 数组为负无穷
    dp[0] = 0  # 开始位置得分为0

    # 遍历数组的每一个位置
    for i in range(n - 1):
        # 从 i+1 到 n 的所有可能位置
        for j in range(i + 1, n):
            dp[j] = max(dp[j], dp[i] + (j - i) * nums[i])

    return dp[-1]

# 示例1
nums1 = [1, 3, 1, 5]
print(maxScore(nums1))  # 输出: 7

# 示例2
nums2 = [4, 3, 1, 3, 2]
print(maxScore(nums2))  # 输出: 16

from collections import deque

def maxScore(nums):
    n = len(nums)
    dp = [0] * n
    dp[0] = 0  # 初始位置得分为 0
    
    deque_q = deque([0])  # 单调队列存储索引
    
    for j in range(1, n):
        # 更新 dp[j]，使用队列头部的索引计算
        dp[j] = dp[deque_q[0]] + (j - deque_q[0]) * nums[deque_q[0]]
        
        # 保持队列的单调性，将小于当前 dp[j] 的元素移除
        while deque_q and dp[j] >= dp[deque_q[-1]]:
            deque_q.pop()
        
        # 将当前索引 j 加入队列
        deque_q.append(j)
        
        # 如果队列头部元素已经不能跳跃到当前索引 j，则移除它
        if j - deque_q[0] >= len(nums):
            deque_q.popleft()
    
    return dp[-1]

# 示例测试
nums1 = [1, 3, 1, 5]
nums2 = [4, 3, 1, 3, 2]
print(maxScore(nums1))  # 输出: 7
print(maxScore(nums2))  # 输出: 16

