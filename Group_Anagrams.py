from typing import List


def isAnagram(word1: str, word2: str) -> bool:
    chars1 = [char for char in word1]
    chars2 = [char for char in word2]
    chars1.sort()
    chars2.sort()
    if chars1 == chars2:
        return True
    return False


class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        list_of_anagrams = []
        while len(strs) != 0:
            referenceWord = strs[0]
            anagram_sublist = [referenceWord]
            strs.remove(referenceWord)
            i = 0
            while i < len(strs):
                if isAnagram(referenceWord, strs[i]):
                    anagram_sublist.append(strs[i])
                    strs.remove(strs[i])
                    i -= 1
                i += 1
            list_of_anagrams.append(anagram_sublist)
        return list_of_anagrams
