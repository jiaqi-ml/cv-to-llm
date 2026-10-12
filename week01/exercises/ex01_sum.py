# ex01_sum.py —— 练习 1：用循环求和
# 运行方式：/opt/anaconda3/bin/python3 ex01_sum.py


# ============ 第一部分：先跑一遍，看清"累加"是怎么发生的 ============
# 这一段是示例，已经写好了。不要改，先运行看输出。

total = 0                                    # 累加变量：准备一个从 0 开始的盒子
for n in [10, 20, 30]:                       # 让 n 依次变成 10、20、30
    total = total + n                        # 把当前的 n 加进盒子
    print("加上", n, "以后，盒子里是", total)   # 每轮打印，看清过程

print("示例最终结果：", total)                 # 应该是 60
print()                                      # 空一行


# ============ 第二部分：现在轮到你了 ============
# 要求：
#   [2, 5, 8] → 15
#   []        → 0
#   不许用 sum()
total = 0
nums = [2, 5, 8]
for n in nums:
    total = total + n
print(total)

total = 0
nums = []
for n in nums:
    total = total + n
print(total)