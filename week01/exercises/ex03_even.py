def even (nums):
    if len(nums) == 0:
        return []

    even_nums = []
    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)

    return even_nums

print(even([1, 2, 3, 4, 6]))  # [2, 4, 6]
print(even([]))