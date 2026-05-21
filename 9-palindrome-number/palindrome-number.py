class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp=x
        new=0
        while temp > 0:
            rem = temp % 10
            temp //= 10
            new = new * 10 + rem
        if x == new:
            return (True)
        else:
            return (False)
    
