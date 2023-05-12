class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest_seq = 0

        for num in nums:
            # check if num is the start of a sequence
            if num - 1 not in num_set:
                curr_seq = 1
                next_num = num + 1
                # check for consecutive numbers
                while next_num in num_set:
                    curr_seq += 1
                    next_num += 1
                longest_seq = max(longest_seq, curr_seq)
        
        return longest_seq