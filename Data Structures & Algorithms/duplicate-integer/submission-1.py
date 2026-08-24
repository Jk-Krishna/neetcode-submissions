class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        h =  {}
        for i in range(len(nums)):
            if nums[i] in h:
                return True
            else:
                h[nums[i]]=i
        return False