class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # will solve this using bucket sort
        # index of the freq list is the number of times that number in the list appears
        freq = [[] for i in range(len(nums)+1)]
        # get the count of all the numbers to be out in the freq buckets
        countMap = {}
        for i in range(len(nums)):
            countMap[nums[i]] = countMap.get(nums[i], 0) + 1
        print(countMap)
        
        # put it into the buckets, where the index is the count
        for number, count in countMap.items():
            # print(number, count)
            freq[count].append(number)
                

        res = []
        # print(freq)
        # go from the back and return k elements
        for i in range(len(nums), 0, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res







        


        