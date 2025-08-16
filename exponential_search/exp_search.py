def binary_search(nums, n, lo, hi) -> int:
    lo = 0
    hi = len(nums)

    while lo < hi:
        mid = int((lo+hi)/2)
        
        if nums[mid] == n:
            return mid
        elif n > nums[mid]:
            lo = mid + 1
        else:
            hi = mid
    
    return -1

def exponential_search(nums, target):
    if nums[0] == n:
        return 0
    n = len(nums)
    i = 1

    while i < n and nums[i] < target:
        i *= 2
    
    if nums[i] == target:
        return i
    
    return binary_search(nums, target, i//2, min(i, n-1))
