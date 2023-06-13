class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        # list of lists
        # forgot the keyword "range"
        freq = [[] for i in range(len(nums)+1)]

        # count the frequences of n, using a map {n -> count}
        for n in nums:
            # have to use the .get method for the 0 as defualt value
            # don't need to do "count[n].get(n , 0)" because n is a param
            count[n] = count.get(n , 0) + 1
        
        # for each index in the freq list, place the n,
        #  where its count == freq[ index]
        # not count.values(), its count.items()
        for n, c in count.items():
            freq[c].append(n)

        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res



        