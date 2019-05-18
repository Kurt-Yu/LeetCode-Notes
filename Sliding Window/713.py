def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
    res, product = 0, 1
    i = j = 0
    while j < len(nums):
        product *= nums[j]
        if product >= k:
            while product >= k and i < len(nums):
                product //= nums[i]
                i += 1
            res += (j + 1 - i)
            j += 1
        else:
            res += (j + 1 - i)
            j += 1
    return res if res >= 0 else 0