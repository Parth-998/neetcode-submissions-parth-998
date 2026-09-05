class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            j1 = target - nums[i]
            for j in range(1, len(nums)):
                if j1 == nums[j] and i != j:
                    return [i, j]
                