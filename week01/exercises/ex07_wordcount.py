# ex07_wordcount.py —— 练习 7：手写词频统计
# 运行方式：/opt/anaconda3/bin/python3 ex07_wordcount.py
#
# 要求：
#   ["ai", "python", "ai"]            →   {"ai": 2, "python": 1}
#   []                                →   {}
#   不许用 Counter
#
# 这是本周主目标（keyword_stats_minimal.py）的核心零件。
# 它 = 练习 5 的"见过没有" + 字典的"取值/赋值"。


# ============ 第一部分：先跑一遍，看清"每处理一个词，字典怎么变" ============
# 这一段是示例，已经写好了。不要改，先运行看输出。

counts = {}                                     # 结果字典：空的，在循环外创建
for word in ["cat", "dog", "cat"]:              # 让 word 依次变成每个词
    if word in counts:                          # 这个词之前出现过吗？
        counts[word] = counts[word] + 1         # 出现过 → 在原数上加 1
    else:
        counts[word] = 1                        # 第一次见 → 记成 1
    print("处理完", word, "后，字典是", counts)   # 每轮打印，看清过程

print("最终词频：", counts)                      # 应该是 {'cat': 2, 'dog': 1}
print()                                         # 空一行

# 现在把上面的 if/else 用 .get() 改写成一行，看看是不是等价：
counts2 = {}
for word in ["cat", "dog", "cat"]:
    counts2[word] = counts2.get(word, 0) + 1    # 没找到就当成 0，再加 1
print("用 .get() 的结果：", counts2)             # 应该和上面一样
print()


# ============ 第二部分：现在轮到你了 ============
# 要求：
#   ["ai", "python", "ai"]  →  {"ai": 2, "python": 1}
#   []                      →  {}
#
# 上面已经给了你两版示范（if/else 版 和 .get() 版），任选一版自己写一遍。
# 注意：演示里的列表是猫狗，你要处理的是 ai/python。不要直接复制不改列表。
#
# 写之前先答：
#   1. counts 这个字典要在循环的里面还是外面创建？为什么？
#   2. 空列表进来时，循环会执行几次？所以结果是什么？
#
# 写在这里：


# ============ 第三部分：把它接上练习 6 ============
# 你有两段能力了：
#   tokenize 能力：一段文本 → 词列表
#   count 能力   ：词列表 → 词频字典
#
# 把它们连起来，就得到本周主工具的骨架：
#   一段文本 → 词列表 → 词频字典
#
# 先在这里用普通代码连一次：
#   text = "  AI python AI  "
#   words = （练习 6 的写法）
#   counts = （练习 7 的写法）
#   print(counts)          → 期望 {"ai": 2, "python": 1}
#
# 写在这里：


# ============ 第四部分：三个用例 ============
#   ["ai", "python", "ai"]   →   {"ai": 2, "python": 1}
#   []                       →   {}
#   文本 "  AI python AI  "   →   {"ai": 2, "python": 1}
#
# 三组都跑通，练习 7 才算过。
