class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1 or n == 4:
            return True
        
        aux = n
        count = 0
        while aux >= 4:
            aux = aux / 4
            count += 1
        return pow(4, count) == n
         


s = Solution()
print(s.isPowerOfFour(20))