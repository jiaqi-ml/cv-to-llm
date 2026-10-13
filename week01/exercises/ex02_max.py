
nums = [4, 1, 9, 6]
champion = nums[0]                              # 先让第一个数当擂主
print("开局擂主：", champion)

for n in nums:                                  # 让 n 依次变成 4、1、9、6
    if n > champion:                            # 挑战者比擂主大吗？
        champion = n                            # 是 → 换人
        print("   ", n, "挑战成功，新擂主是", champion)
    else:
        print("   ", n, "挑战失败，擂主仍是", champion)

print("示例最终擂主：", champion)                 # 应该是 9
print()                                         # 空一行



nums = [3,9,2,7]
champion = nums[0]                              # 先让第一个数当擂主
print("开局擂主：", champion)

for n in nums:                                  # 让 n 依次变成 4、1、9、6
    if n > champion:                            # 挑战者比擂主大吗？
        champion = n                            # 是 → 换人
        print("   ", n, "挑战成功，新擂主是", champion)
    else:
        print("   ", n, "挑战失败，擂主仍是", champion)

print("示例最终擂主：", champion)                 # 应该是 9
print()  


nums = [-5,-1,-9]
champion = nums[0] 
print("开局擂主：", champion)
for n in nums:                                  # 让 n 依次变成 4、1、9、6
    if n > champion:                            # 挑战者比擂主大吗？
        champion = n                            # 是 → 换人
        print("   ", n, "挑战成功，新擂主是", champion)
    else:
        print("   ", n, "挑战失败，擂主仍是", champion)

print("示例最终擂主：", champion)                 # 应该是 9
print()  
                                       # 空一行
def check(nums):
    if len(nums) == 0:
        return None

print("空列表的结果：", check([]))


