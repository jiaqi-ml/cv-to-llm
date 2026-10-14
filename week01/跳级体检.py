# 跳级体检.py —— 用证据决定能不能跳过 Python 基础期（W1—W3）
#
# 为什么有这个文件：
#   「代码基础跳过，需要时用大模型补」这个决定，只有在能当场拿出证据时才是安全的。
#   本文件就是那次取证：15 道自动判分的小题，跑一次就知道该从哪一周开始。
#
# 规则：
#   第 1 档  闭卷（不查资料、不用 AI、不看旧代码），限时 30 分钟。这是 W1 的正式验收。
#   第 2 档  可以查官方文档（W2 还没学，目的只是探边界），限时 20 分钟。
#   第 3 档  可以查官方文档，限时 20 分钟。
#
# 运行：
#   /opt/anaconda3/bin/python3 /Users/qi/study/cv-to-llm/week01/跳级体检.py
#
# 结果怎么用：
#   第 1 档 6/6 → W1 剩余练习只做没掌握的，直接进 W2 内容
#   第 2 档 5/5 → W2 的函数/文件/异常主干可跳过
#   第 3 档 4/4 → W3 的 JSON 主干可跳过，下一步进 W4 NumPy
#   任何一档未满 → 只补没 PASS 的那几题，不重听整周课
#
# 判分在文件末尾，不要改。你只写上面六个函数体里的 pass。

import json
import os
import tempfile


# ============================================================
# 第 1 档：W1 核心（闭卷 30 分钟）
# ============================================================

def count_items(items):
    """统计每个元素出现的次数。
    ["ai", "cv", "ai"] -> {"ai": 2, "cv": 1}
    []                 -> {}
    不许用 collections.Counter
    """
    # 写在这里（删掉下面的 pass）
    pass


def filter_scores(scores, threshold):
    """保留 >= threshold 的分数，保持原来的顺序。
    [55, 60, 90, 59], 60 -> [60, 90]
    [], 60               -> []
    """
    # 写在这里（删掉下面的 pass）
    pass


def top_k(counts, k):
    """按次数从多到少取前 k 个，返回 [("词", 次数), ...]。
    {"ai": 3, "cv": 1, "python": 2}, 2 -> [("ai", 3), ("python", 2)]
    {}, 2                              -> []
    次数相同时按词本身从小到大排（保证结果唯一，方便判分）
    """
    # 写在这里（删掉下面的 pass）
    pass


# ============================================================
# 第 2 档：W2 函数 / 文件 / 异常（可查文档，20 分钟）
# ============================================================

def summarize(records, key="score"):
    """records 形如 [{"name": "a", "score": 80}, {"name": "b", "score": 90}]
    返回 (记录总条数, 该字段的平均值)。
      []                      -> (0, None)
      全都缺 key 字段          -> (条数, None)
    缺少 key 字段的记录要计入条数，但不计入平均。
    """
    # 写在这里（删掉下面的 pass）
    pass


def read_text(path):
    """用 UTF-8 读入整个文本文件并返回字符串。
    文件不存在时返回 None，不要崩溃。
    """
    # 写在这里（删掉下面的 pass）
    pass


# ============================================================
# 第 3 档：W3 JSON（可查文档，20 分钟）
# ============================================================

def save_json(obj, path):
    """把 obj 写成 UTF-8 的 JSON 文件。
    中文要原样保留，不要变成 u4e2d 那种转义形式。
    """
    # 写在这里（删掉下面的 pass）
    pass


def load_json(path):
    """读回 JSON 并返回对应的 Python 对象；文件不存在时返回 None。"""
    # 写在这里（删掉下面的 pass）
    pass


# ============================================================
# 以下是自动判分，不要改
# ============================================================

_results = []


def check(label, fn, expected):
    try:
        got = fn()
    except Exception as exc:
        print("  FAIL  " + label)
        print("        报错 " + type(exc).__name__ + ": " + str(exc))
        _results.append(False)
        return
    ok = got == expected
    print(("  PASS  " if ok else "  FAIL  ") + label)
    if not ok:
        print("        得到 " + repr(got))
        print("        期望 " + repr(expected))
    _results.append(ok)


def _tier(start):
    return sum(1 for ok in _results[start:] if ok)


def main():
    tmp = tempfile.mkdtemp(prefix="probe_")
    has_text = os.path.join(tmp, "ok.txt")
    with open(has_text, "w", encoding="utf-8") as f:
        f.write("你好\nAI python\n")
    no_file = os.path.join(tmp, "missing.txt")
    json_path = os.path.join(tmp, "out.json")

    print("第 1 档：W1 核心（闭卷 30 分钟）")
    start = len(_results)
    check('count_items(["ai","cv","ai"])',
          lambda: count_items(["ai", "cv", "ai"]), {"ai": 2, "cv": 1})
    check("count_items([])", lambda: count_items([]), {})
    check("filter_scores([55,60,90,59], 60)",
          lambda: filter_scores([55, 60, 90, 59], 60), [60, 90])
    check("filter_scores([], 60)", lambda: filter_scores([], 60), [])
    check('top_k({"ai":3,"cv":1,"python":2}, 2)',
          lambda: top_k({"ai": 3, "cv": 1, "python": 2}, 2), [("ai", 3), ("python", 2)])
    check("top_k({}, 2)", lambda: top_k({}, 2), [])
    t1 = _tier(start)

    print()
    print("第 2 档：W2 函数 / 文件 / 异常（可查文档）")
    start = len(_results)
    check("summarize 正常输入",
          lambda: summarize([{"name": "a", "score": 80}, {"name": "b", "score": 90}]), (2, 85.0))
    check("summarize 空列表", lambda: summarize([]), (0, None))
    check("summarize 缺字段",
          lambda: summarize([{"name": "a"}, {"name": "b"}]), (2, None))
    check("read_text 存在文件", lambda: read_text(has_text), "你好\nAI python\n")
    check("read_text 不存在文件",
          lambda: (read_text(has_text), read_text(no_file)),
          ("你好\nAI python\n", None))
    t2 = _tier(start)

    print()
    print("第 3 档：W3 JSON（可查文档）")
    start = len(_results)
    check("save_json + load_json 往返",
          lambda: (save_json({"a": 1, "b": [1, 2]}, json_path), load_json(json_path))[1],
          {"a": 1, "b": [1, 2]})
    check("load_json 不存在文件",
          lambda: (save_json({"z": 1}, json_path), load_json(json_path), load_json(no_file))[1:],
          ({"z": 1}, None))
    check("save_json 中文不转义",
          lambda: (save_json({"中文": "值"}, json_path),
                   "中文" in open(json_path, encoding="utf-8").read())[1],
          True)
    check("save_json 空字典往返",
          lambda: (save_json({}, json_path), load_json(json_path))[1],
          {})
    t3 = _tier(start)

    print()
    print("=" * 56)
    print("第 1 档 %d/6    第 2 档 %d/5    第 3 档 %d/4" % (t1, t2, t3))
    print("=" * 56)
    if t1 == 6:
        print("W1：基础已达标 -> 剩余练习只挑没掌握的，直接进 W2 的函数与文件内容。")
    else:
        print("W1：只补没 PASS 的那几题，不要重听整周。")
    if t2 == 5:
        print("W2：函数 / 文件 / 异常主干可跳过。")
    if t3 == 4:
        print("W3：JSON 主干可跳过 -> 下一步进 W4 NumPy，把省下的时间加给项目。")


main()
