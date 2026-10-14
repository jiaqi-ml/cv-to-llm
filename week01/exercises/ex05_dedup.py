# ex05_dedup.py —— 练习 5：保持顺序去重
# 运行方式：/opt/anaconda3/bin/python3 ex05_dedup.py
# 要求：不用 set()


# ============ 第一部分：先跑一遍，看清"见过没有"是怎么判断的 ============
# 这一段是示例，已经写好了。不要改，先运行看输出。

# seen = []                                       # 结果列表：放"已经见过"的词
# for word in ["cat", "dog", "cat", "bird"]:      # 让 word 依次变成每个词
#     if word in seen:                            # word 已经在 seen 里了吗？
#         print(word, "→ 见过了，跳过")
#     else:
#         seen.append(word)                       # 没见过 → 收进结果
#         print(word, "→ 第一次见，收下")

# print("去重结果：", seen)                         # 应该是 ['cat', 'dog', 'bird']
# print()                                         # 空一行


# ============ 第二部分：现在轮到你了 ============
# 要求：
#   ["ai", "cv", "ai", "python"]  →  ["ai", "cv", "python"]   保留第一次出现的顺序
#   []                            →  []
#   不许用 set()
#
# 两个要想清楚的问题（写之前先答出来）：
#   1. 结果列表要在循环的里面还是外面创建？为什么？
#   2. 判断"见过没有"用哪个关键字？
#
# 写在这里：


aii = []
for i in ["ai", "cv", "ai", "python"]:
    if i in aii:
        print(i, "→ 见过了，跳过")
    else:
        aii.append(i)
        print(i, "→ 第一次见，收下")
print("去重结果：", aii)
aii = []
for i in []:
    if i in aii:
        print(i, "→ 见过了，跳过")
    else:
        aii.append(i)
        print(i, "→ 第一次见，收下")
print("空列表结果：", aii)