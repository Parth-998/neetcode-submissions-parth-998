class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_1 = []
        for i in nums:
            if i not in nums_1:
                nums_1.append(i)
            else:
                return True
        return False