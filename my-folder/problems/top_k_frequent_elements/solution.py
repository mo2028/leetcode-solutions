class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap  = {}
        for n in nums:
            countMap[n] = countMap.get(n, 0)+1

        freq_list = list(countMap.items())
        freq_list.sort(key=lambda x: x[1], reverse=True)
        print(freq_list)

        freq = []
        for i in range(k):
            freq.append(freq_list[i][0])
        return freq




        