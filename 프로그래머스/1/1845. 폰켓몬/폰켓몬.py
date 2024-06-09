def solution(nums):
    a = dict()
    for i in nums:
        a[i] = 1
    return min (len(nums)//2, len(a))