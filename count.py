#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, string
from rich.progress import track

if __name__ == "__main__":
    cnt_en, cnt_zh, cnt_dg, cnt_pu = [0] * 4
    filepaths = [
        os.path.abspath(os.path.join(dirpath, filename))
        for dirpath, dirnames, filenames in os.walk(".")
        for filename in filenames
        if str(filename).endswith(".md")
    ]
    for filepath in track(filepaths):
        with open(filepath, encoding="utf-8") as f:
            for line in f:
                for c in line:
                    if c in string.ascii_letters:  # 英文
                        cnt_en += 1
                    elif c.isalpha():  # 中文, isalpha()会得到英文和中文, 但是英文已经在上面的if筛选了
                        cnt_zh += 1
                    elif c.isdigit():  # 数字
                        cnt_dg += 1
                    elif c.isspace():  # 空格
                        pass
                    else:  # 标点符号
                        cnt_pu += 1

    print(f"总共{len(filepaths)}篇文章")
    print(f"字母:{int(cnt_en):,d}个")
    print(f"汉字:{int(cnt_zh):,d}字")
    print(f"数字:{int(cnt_dg):,d}位")
    print(f"标点:{int(cnt_pu):,d}个")
    print(f"总共大约:{int(cnt_zh + cnt_en//6 + cnt_dg//32):,d}字")  # fmt: skip
