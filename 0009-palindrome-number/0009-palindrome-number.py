class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = list(str(x))
        if len(x) == 2 and x[0] != x[1]:
            return False
        for i in range(1, len(x)//2+1):
            if x[i-1] != x[-i]:
                return False
        return True