class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}  
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i

        return -1
    
s = Solution()
print(s.twoSum([2,7,11,15], 9))