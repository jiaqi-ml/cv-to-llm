def check(nums):
    if len(nums) == 0:
        return None

    total = 0
    for num in nums:
        total += num

    average = total / len(nums)
    return average


print(check([2, 4, 6]))  # 4.0
print(check([1]))        # 1.0
print(check([1, 2]))     # 1.5
print(check([]))         # None