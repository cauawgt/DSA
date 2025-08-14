class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res = ''
        tam = len(s)
        i = 0
        
        while tam >= 2*k:
            aux = s[i:i + 2*k]
            res += aux[:k][::-1] + aux[k:]
            tam -= 2*k
            i += 2*k 
        
        aux = s[i:]
        if tam < k:
            res += aux[::-1]
        else:  
            res += aux[:k][::-1] + aux[k:]
        
        return res
    
    def reverseStr2(self, s: str, k: int) -> str:
         res = []
         for i in range(0, len(s), 2*k):
            bloco = s[i:i + 2*k]
            res.append(bloco[:k][::-1] + bloco[k:])

s = Solution()
print(s.reverseStr('abcdefg', 2))