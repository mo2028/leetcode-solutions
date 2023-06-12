class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = defaultdict(list)
        

        for s in strs:
            count = [0]*26
            for letter in s:
                count[ord(letter) - ord("a")] += 1
            anagram_groups[tuple(count)].append(s)
        return anagram_groups.values()

