class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        pivot = 0
        
        for i in range(1, len(nums)):
            print(i, nums[i], pivot)

            if nums[i] != nums[pivot]:
                # next is unique, move to current pivot position
                pivot += 1
                nums[pivot] = nums[i]
            # else:
                # next is the same, don't move pivot
                
        return pivot + 1


s = Solution()
nums = [1, 1, 2]
nums = [1,1,1,2,2,3,6,7,8]
nums = []
lenght = s.removeDuplicates(nums)
print(nums, lenght)