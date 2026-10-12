# ex02_max.py —— 练习 2：用循环找最大值
# 运行方式：/opt/anaconda3/bin/python3 ex02_max.py


# ============ 第一部分：先跑一遍，看清"擂主"是怎么换人的 ============
# 这一段是示例，已经写好了。不要改，先运行看输出。

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


# ============ 第二部分：现在轮到你了 ============
# 要求：
#   [3, 9, 2, 7]   → 9
#   [-5, -1, -9]   → -1      （全是负数也要对）
#   []             → None    （空列表：连擂主都没有，直接返回 None）
#   不许用 max()
#
# 为什么不能直接写 champion = nums[0]？
#   因为 nums 是空列表时，nums[0] 会报 IndexError: list index out of range。
#   所以要先用 len() 拦住空列表。
#
# 步骤：
#   1) nums = [3, 9, 2, 7]
#   2) if len(nums) == 0:     然后 print(None) —— 空列表走这条，到此结束
#   3) else:                  非空走这条，里面做三步：
#          champion = nums[0]      第一个数当擂主
#          for n in nums:          遍历
#              if n > champion:    挑战
#                  champion = n
#          print(champion)         循环结束后打印
#   4) 把 nums 换成 [-5, -1, -9] 再跑一次，应该是 -1
#   5) 把 nums 换成 [] 再跑一次，应该是 None
