class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)): return False
#Creates a list for each word containing its respective characters
        list1 = [char for char in s]
        list2 = [char for char in t]
        list1.sort()
        list2.sort()
        print(list1, list2)
        if (list1 == list2):
            return True
        return False
