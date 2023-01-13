# https://leetcode.com/problems/maximum-gap/
nums = [1, 1, 1, 1, 5, 5, 5, 5]
nums.sort()
gap = []

def maximumGap(nums) -> int:
    gap = []
    for i, num in enumerate(nums):
        gap.append(nums[(i+1) % len(nums)] - num)
        print(gap)
    return max(gap)

gap = maximumGap(nums)
print(gap)