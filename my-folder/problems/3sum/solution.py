class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the numbers
        nums.sort()

        # init result list
        result = []


        # outer for loop that costs O(n)
        for i in range(len(nums) - 2):


            # skip duplicate of i 
            # forgot about this if statement and handeling the case of the dulicates of i
            if i > 0 and nums[i] == nums[i-1]:
                continue 


            # init left and right 
            l = i + 1
            r = len(nums) - 1


            # while loop 2 sum
            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]

                
                # if statements to move the pointers
                if threeSum < 0:
                    l+=1
                elif threeSum > 0:
                    r-=1
                else:
                    result.append([nums[i], nums[l], nums[r]])

                    # while loops to make sure you skip the dupicated
                    # the below while loops were outsie of the else before, and think about why it has to be inside the else statement 
                    while l < r and nums[l] == nums[l+1]:
                        l += 1

                    while l < r and nums[r] == nums[r-1]:
                        r -= 1


                    # i had a quesiton about whether to include the below updation
                    # the below code is absolutely needed because, the while loops only execute if there are duplicates and if there are no duplicates, 
                    # we still need to update it using the code below
                    l += 1
                    r -= 1

        return result       

            
