from typing import List

class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        n = len(b)
        # 初始化最大得分为负无穷大
        max_score = -float('inf')

        # 我们需要依次选择 4 个 b 的下标
        # 贪心地从前到后找到符合要求的组合
        # 维护四个变量分别代表 b[i0], b[i1], b[i2], b[i3] 的最大值
        max1 = -float('inf')
        max2 = -float('inf')
        max3 = -float('inf')
        max4 = -float('inf')
        
        for i in range(n):
            # 选择 b[i] 对应的最大可能的得分
            if i >= 3:
                max4 = max(max4, max3 + a[3] * b[i])
            if i >= 2:
                max3 = max(max3, max2 + a[2] * b[i])
            if i >= 1:
                max2 = max(max2, max1 + a[1] * b[i])
            max1 = max(max1, a[0] * b[i])
        
        return max4  # 最终返回四个值的最大组合

# 示例测试
solution = Solution()
print(solution.maxScore([3, 2, 5, 6], [2, -6, 4, 5, -3, 2]))  # 输出应为26
print(solution.maxScore([-1, 4, 5, -2], [-5, -1, 3, -2, -4]))  # 输出应为-1
