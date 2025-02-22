class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = [[] for i in range(len(nums)+1)]
        count = {}
        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0)+1
        # print(count)

        for n, cnt in count.items():
            freq[cnt].append(n)

        for i in range(len(freq)-1, 0, -1):
            for u in freq[i]:
                res.append(u)
                if len(res) == k:
                    return res


        