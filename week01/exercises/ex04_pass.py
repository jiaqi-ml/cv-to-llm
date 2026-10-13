def passs(nums):
    if len(nums) == 0:
        return 0

    totalpass = 0

    for i in nums:
        if i >= 60:
            totalpass = totalpass + 1

    return totalpass


print(passs([50, 60, 80, 59]))
print(passs([60]))
print(passs([]))