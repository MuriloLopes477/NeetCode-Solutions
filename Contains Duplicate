class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        Set = {""}
        for i in nums:
# Checks to see if set size changes each time an element from list is added to Set, if not, there is at least one duplicate
            original = len(Set)
            Set.add(i)
            new = len(Set)
            if original == new:
                return True
        return False
