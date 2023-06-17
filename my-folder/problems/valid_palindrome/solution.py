class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 2. init left and right pointers 
        l, r = 0, len(s)-1

        # forgot the main l<r loop that drives the whole thing
        while l < r:
            # 4. while loops to forward or backwads the pointer if not alphanumeric
            # forgot the self.isAlphanumeric and the l < r
            while l < r and not self.isAlphaNumeric(s[l]):
                l += 1
            while l < r and not self.isAlphaNumeric(s[r]):
                r -= 1
        
            # 3. while loop to check if the left and right character are the same
            # what is .lower?
            # I had "while s[l].lower() != s[r].lower():", it it just a check once
            if s[l].lower() != s[r].lower():
                return False
        
            # 5. update forward and bakcward pointers
            # if the program reached here it means that it is okay to update
     
            l += 1
            r -= 1

        # if it gets out of the loop successfully then return true
        return True




    # 1. first  write a function to check if a character is alpha numeric
    # had this indented inside the isPalindrome function, which is wrong becuase it is a class method of Solution. 
    def isAlphaNumeric(self, c):
        return (ord("A") <= ord(c) <= ord("Z") or 
                ord("a") <= ord(c) <= ord("z") or
                ord("0") <= ord(c) <= ord("9"))