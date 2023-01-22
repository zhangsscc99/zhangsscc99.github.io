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
    def sortArray(self,nums):
        print('haha')
        for i in range(1,len(nums)):
            value=nums[i]
            j=i-1
            while j>=0 and nums[j]>value:
                nums[j+1]=nums[j]
                j-=1
            nums[j+1]=value
        return nums
s=Solution()
print(s.sortArray([2,1,3,5,4]))