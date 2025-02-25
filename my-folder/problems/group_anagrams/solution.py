class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupAnagrams = defaultdict(list)
        for i in range(len(strs)):
            keyCount = [0]*26
            for s in strs[i]:
                keyCount[ord(s) - ord('a')] += 1
            groupAnagrams[tuple(keyCount)].append(strs[i])
            
        return list(groupAnagrams.values())