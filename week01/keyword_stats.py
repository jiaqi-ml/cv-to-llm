#!/usr/bin/env python3
"""关键词统计工具 —— W1 骨架（请自己实现，不要用 AI 生成后直接粘贴）

用途：读取一个文本文件（或目录下所有 .txt），统计词频，输出出现最多的前 N 个词。
本文件只给出结构、类型约定和 TODO。函数体请自己写。

运行方式（实现后）：
    python3 keyword_stats.py --input sample.txt --top-k 10
    python3 keyword_stats.py --input ./docs --top-k 10 --json
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def read_text(path: Path) -> str:
    """读取单个文本文件内容。

    要求：
      - 用 with open(...) 并显式指定 encoding="utf-8"
      - 文件不存在时不要崩溃：捕获 FileNotFoundError，返回空字符串
    提示：中文文本可能带 BOM，留意 encoding="utf-8-sig" 的情况。
    """
    # TODO: 你自己实现
    raise NotImplementedError


def collect_texts(input_path: Path) -> list[tuple[str, str]]:
    """把输入统一成 [(来源名, 文本内容), ...]。

    要求：
      - 如果 input_path 是文件：返回 1 个元素
      - 如果是目录：扫描其下所有 *.txt（用 Path.glob），逐个读入
      - 目录里一个 .txt 都没有时，返回空列表（不要报错）
    """
    # TODO: 你自己实现
    raise NotImplementedError


def tokenize(text: str) -> list[str]:
    """把文本切成词。

    要求（先做最简版，别用正则库里的高级特性）：
      - 英文：按空白切分，转小写
      - 中文：先按字符或按空白切（本周末再改进）
      - 丢掉空字符串
    注意：返回的是 list，不是 set（因为要计数）。
    """
    # TODO: 你自己实现
    raise NotImplementedError


def count_words(tokens: list[str]) -> dict[str, int]:
    """统计词频。

    要求：
      - 空列表返回空字典 {}
      - 用 dict 或 collections.Counter 都行，但你要能解释区别
    """
    # TODO: 你自己实现
    raise NotImplementedError


def top_k(counter: dict[str, int], k: int) -> list[tuple[str, int]]:
    """返回出现次数最多的前 k 个 (词, 次数)。

    要求：
      - 次数相同时按词本身排序，保证结果稳定（每次运行输出一致）
        —— 提示：sorted 的 key 可以返回元组
      - k 大于总词数时，返回全部，不要报错
      - 空字典返回空列表
    """
    # TODO: 你自己实现
    raise NotImplementedError


def format_plain(items: list[tuple[str, int]]) -> str:
    """人类可读输出，每行格式：`词    次数`"""
    # TODO: 你自己实现
    raise NotImplementedError


def format_json(items: list[tuple[str, int]]) -> str:
    """JSON 输出。

    要求：
      - ensure_ascii=False（否则中文变成 \\uXXXX）
      - indent=2
    """
    # TODO: 你自己实现
    raise NotImplementedError


def build_parser() -> argparse.ArgumentParser:
    """命令行参数。

    要求（示例）：
      --input / -i   必填，文件或目录路径
      --top-k / -k   可选，默认 10，类型 int
      --json         可选开关（store_true），输出 JSON 而非纯文本
    """
    # TODO: 你自己实现
    raise NotImplementedError


def main() -> int:
    """串起全流程，返回退出码（0 表示正常）。

    要求：
      - 读不到任何文本时，打印一句提示到 stderr 并返回非 0
      - 正常时把结果打印到 stdout
    """
    # TODO: 你自己实现
    raise NotImplementedError


if __name__ == "__main__":
    raise SystemExit(main())
