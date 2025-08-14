class Solution:
    def reverseWords(self, s: str) -> str:
        l, r = 0, 0
        t = ''
        while r < len(s):
            if s[r] == ' ':
                pular = r
                r -= 1
                while r != l:
                    t += s[r]
                    r -= 1
                t += s[r]
                t += s[pular]
                r = pular + 1
                l = pular + 1
            elif r == len(s) - 1:
                while r >= l:
                    t += s[r]
                    r -= 1
                r = len(s) # break
            else:
                r += 1
        return t
    
    def reverseWords2(self, s:str) -> str:
        res = ''
        l, r = 0, 0

        while r < len(s):
            if s[r] != ' ':
                r += 1
            else:
                res += s[l:r+1][::-1]

                r += 1
                l = r

        res += ' '
        res += s[l:r+2][::-1]
        return res[1:]
    
s = Solution()

print(s.reverseWords2("Let's take LeetCode contest"))