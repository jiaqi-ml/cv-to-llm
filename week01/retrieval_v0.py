#!/usr/bin/env python3
"""文档检索器 v0 —— 纯 Python 倒排索引（W1 骨架，请自己实现）

这是 W3 向量检索的雏形，也是 P1（多模态文档检索）的第一块砖。
本周只用 dict / list / str，不许用 numpy、不许用任何第三方库。

原理：倒排索引 = {词: {文档号, ...}}
  建索引时：遍历每篇文档的每个词，把这个文档号加进该词的集合
  检索时：把查询也切词，找出包含任一查询词的文档，按"命中不同词的数量"排序

运行方式（实现后）：
    python3 retrieval_v0.py
（自带一个小 demo 语料，直接跑就能看到检索结果）
"""

from __future__ import annotations


class InvertedIndex:
    """倒排索引。

    设计约定：
      - self.docs:      dict[int, str]        文档号 -> 原文
      - self.inverted:  dict[str, set[int]]   词 -> 包含它的文档号集合
      - self._next_id:  int                   下一篇文档的编号
    """

    def __init__(self) -> None:
        # TODO: 初始化上面三个属性
        raise NotImplementedError

    # ---------- 建索引 ----------

    def tokenize(self, text: str) -> list[str]:
        """切词。要求与 keyword_stats.tokenize 保持一致。

        本周先做最简版：按空白切、转小写、去空串。
        如果你想让中文可检索，可以把中文按字符切开——但要能解释代价。
        """
        # TODO
        raise NotImplementedError

    def add_document(self, text: str) -> int:
        """加入一篇文档，返回它的文档号。

        要求：
          - 空文本也要能加入（占一个文档号，只是不产生任何倒排项）
          - 同一文档内重复出现的词，在 set 里只算一次
        """
        # TODO
        raise NotImplementedError

    # ---------- 检索 ----------

    def search(self, query: str, top_k: int = 3) -> list[tuple[int, int]]:
        """检索，返回 [(文档号, 命中词数), ...]，按命中词数降序。

        要求：
          - 查询为空 / 切不出词时，返回空列表
          - 命中词数相同时，按文档号升序（保证结果稳定）
          - 一个词都没命中时返回空列表
          - **不要**在遍历 set 的过程中修改它（这是本周要练的一个坑）
        """
        # TODO
        raise NotImplementedError

    def stats(self) -> dict[str, int]:
        """返回 {"num_docs": ..., "num_terms": ...}，供你观察索引规模。"""
        # TODO
        raise NotImplementedError


def demo() -> None:
    """小 demo：3—5 篇短文，跑几个查询，打印结果。

    建议的查询：
      - 一个能命中的词
      - 一个命中多个文档的词（看排序）
      - 一个完全不存在的词（应返回空列表）
      - 空字符串（应返回空列表）
    """
    corpus = [
        "多模态大模型需要处理图像和文本",          # doc 0
        "检索增强生成在文档问答中很常用",          # doc 1
        "向量检索是文档问答的基础组件",            # doc 2
        "python 基础语法包括列表和字典",           # doc 3
    ]

    # TODO:
    # 1. 建索引并加入 corpus
    # 2. 打印 stats()
    # 3. 逐个查询并打印 search() 结果，同时打印命中的文档原文，便于肉眼检查对不对
    raise NotImplementedError


if __name__ == "__main__":
    demo()
