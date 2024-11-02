class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
# Iterates and searches for valid combination of values that sum to target      
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                current = nums[i] + nums[j]
                if current == target:
# Returns the indexes for the values that add up to target
                    return [i, j]

        return [0, 0]
