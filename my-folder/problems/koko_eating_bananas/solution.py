class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        res = r

        while l <= r:
            middle = (l+r) // 2

            hours = 0
            for p in piles:
                hours += math.ceil( float(p) / middle)

            if hours <= h:
                res = middle
                r = middle - 1
            else:
                l = middle + 1

        return res
    
    