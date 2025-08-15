class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        l, r = 0, 0
        alfabet = set(s)
        maximo = 0

        d = dict()
        for i in alfabet:
            d[i] = 0
            
        while r < len(s):
            char = s[r]
            d[char] += 1
            
            while d.get(char) == 3:
                d[s[l]] -= 1
                l += 1

            if len(s[l:r+1]) > maximo:
                maximo = len(s[l:r+1])
            r += 1

        return maximo

    
    def maximumLengthSubstring2(self, s: str) -> int:
        l, r = 0, 0
        _max = 1
        counter = {}

        counter[s[0]] = 1
         
        while r < len(s) - 1:
            r += 1
            if counter.get(s[r]):
                counter[s[r]] += 1
            else:
                counter[s[r]] = 1
            
            while counter(s[r]) == 3:
                counter[s[l]] -= 1
                l += 1
            
            _max = max(_max, r-l+1)
        
        return _max


s = Solution()
print(s.maximumLengthSubstring('eebadadbfa'))