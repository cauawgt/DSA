class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for idx, char in enumerate(s):
            if d.get(char):
                d[char][1] += 1
            else:
                d[char] = [idx, 1]
        
        for ch, val in d.items():
            if val[1] == 1:
                return val[0]
        
        return -1

s = Solution()
print(s.firstUniqChar('leetcode'))