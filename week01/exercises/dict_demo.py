# dict_demo.py —— 字典示例（周三上午的"看一个小例子"环节）
# 运行方式：/usr/bin/env 不用管，直接：
#   /opt/anaconda3/bin/python3 dict_demo.py
#
# 这个文件是给你"看"的，不是给你"交"的。看完之后改输入、看输出，然后关掉它自己写。


# ============ 1. 字典长什么样 ============
student = {"name": "小明", "age": 20, "score": 88}
print("整个字典：", student)


# ============ 2. 取值：方括号 ============
print("姓名：", student["name"])
print("分数：", student["score"])


# ============ 3. 赋值：往字典里放东西 / 改东西 ============
student["score"] = 95                      # 键已存在 → 改掉原来的值
print("改完分数：", student)

student["city"] = "杭州"                    # 键不存在 → 新建一条
print("加完城市：", student)


# ============ 4. 用 in 判断键在不在 ============
print()
print('"name" in student      ->', "name" in student)
print('"phone" in student     ->', "phone" in student)


# ============ 5. 用方括号取一个不存在的键 = 报错 ============
print()
print("下面这行故意会报错，看 traceback 最后一行：")
print()

# 把下一行开头的 # 去掉，再运行一次，你会看到 KeyError
# print(student["phone"])


# ============ 6. 用 .get() 取不存在的键 = 不报错 ============
print('student.get("phone")          ->', student.get("phone"))
print('student.get("phone", "没填")  ->', student.get("phone", "没填"))
print('student.get("name")           ->', student.get("name"))


# ============ 7. 遍历字典 ============
print()
for key in student:
    print("键：", key, "  值：", student[key])


# ============ 8. 你自己改的地方 ============
# 试着做这几件事，每做一件就重新运行一次，看输出怎么变：
#
#   1. 把 age 改成你的真实年龄（用 student["age"] = ... 而不是改第 9 行）
#   2. 加一个键 "major"，值是 "计算机视觉"
#   3. 用 .get() 取 "major" 和取 "phone"，比较两者的区别
#   4. 把第 34 行的 # 去掉，运行，把报错原文抄进 debug_log.md 的记录 4
#
# 做完这四件事，你就具备写练习 7（词频统计）的全部零件了。
