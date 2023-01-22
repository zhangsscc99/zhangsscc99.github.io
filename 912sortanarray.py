class Solution():
    def sortArray(self, nums):
            """
            :type nums: List[int]
            :rtype: List[int]
            """
            for i in range(len(nums)):
                for j in range(len(nums)-1-i):
                    if nums[j]>nums[j+1]:
                        temp=nums[j]
                        nums[j]=nums[j+1]
                        nums[j+1]=temp
            return nums
s=Solution()
print(s.sortArray([2,1,3,5,4]))