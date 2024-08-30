
def findLengthOfLCIS(nums):
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                dp[i] = dp[i - 1] + 1
        return max(dp)

nums = [2,1,200,100,99]
print(findLengthOfLCIS(nums))