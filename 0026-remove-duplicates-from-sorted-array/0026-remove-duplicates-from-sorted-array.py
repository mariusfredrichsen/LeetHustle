class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        c = 0
        c_1 = len(nums)
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                nums.pop(i+1)
                c += 1
            else:
                i += 1
        return c_1 - c




