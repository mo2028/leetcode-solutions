class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        my_dict = {}
        anagram_dict = {}
        
        for alpha in s:
            my_dict[alpha] = my_dict.get(alpha, 0) + 1

        for alpha in t:
            anagram_dict[alpha] = anagram_dict.get(alpha, 0) + 1

        for alpha in t:
            if anagram_dict.get(alpha, 0) != my_dict.get(alpha, 0):
                return False
        
        return True
