class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        l, r, i = 0, k-1, 0
        result = []
        _max = nums[l]

        while r < len(nums):
            _max = nums[l]
            while i <= r:
                aux = nums[i]
                if aux > _max:
                    _max = aux
                i += 1
            
            result.append(_max)

            l += 1
            i = l
            r += 1
        return result

s = Solution()
print(s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
print(s.maxSlidingWindow([1, -1], 1))