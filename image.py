#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, re, urllib.parse
import asyncio, aiofiles, aiohttp
from rich.progress import track
from typing import Callable


# 全局常量
NOTEPATH = os.path.dirname(os.path.abspath(__file__))
NOTENAME = os.path.basename(NOTEPATH)


# 辅助函数
def get_filepaths():
    return [
        os.path.abspath(os.path.join(dirpath, filename))
        for dirpath, dirnames, filenames in os.walk(".")
        for filename in filenames
        if str(filename).endswith(".md")
    ]


# 切换图床
def change():
    baseurl = "https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource"
    dirname = re.escape(NOTENAME)

    filepaths = get_filepaths()
    for filepath in track(filepaths):
        filename = re.escape(os.path.basename(filepath))
        # midpath like / or /.../
        midpath = re.findall(f"(?<={dirname})(.*?)(?={filename})", filepath)[0]

        def process(link):
            result = baseurl + midpath + os.path.basename(link)
            if result != link:  # 这里可输出需要替换的路径(但是不会输出哪个文件)
                print(result, link)
            return baseurl + midpath + os.path.basename(link)

        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        content = convert_image_links(content, process)

        print("写回被注释")
        # 如果担心搞坏整个项目可以先将写会注释
        # with open(filepath, "w", encoding="utf-8") as f:
        #     f.write(content)


def convert_image_links(content: str, func: Callable[[str], str]) -> str:
    # 黑盒魔法
    pattern = r"!\[.*?\]\((.*?)\)|<img.*?src=[\'\"](.*?)[\'\"].*?>"

    def modify(match):
        link = match.group(1) or match.group(2)
        return str(func(link)).join(match.group().split(link))

    return re.sub(pattern, modify, content)


# 检测笔记中所有链接(链接和图片)
def check():
    asyncio.run(main())


async def main():
    md_files = get_filepaths()
    await asyncio.gather(*[process_md_file(file) for file in md_files])


async def process_md_file(file):
    async with aiofiles.open(file, mode="r") as f:
        content = await f.read()
        patterns = [r"\[.*?\]\((.*?)\)",r"<img.*?src=[\'\"](.*?)[\'\"].*?>",r"<a.*?href=[\'\"](.*?)[\'\"].*?>"]  # fmt: skip
        all_links = [item for pattern in patterns for item in re.findall(pattern, content)]  # fmt: skip
        results = await asyncio.gather(*[check_link(url) for url in all_links])
        for url, status in results:
            if status == 0:
                url = urllib.parse.unquote(url)
                if not check_md_relative_jump(file, url):
                    print(f"{url} in {file} is invalid")


async def check_link(url):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.head(url, allow_redirects=True) as response:
                return url, response.status
        except:
            return url, 0


def check_md_relative_jump(filepath: str, link: str) -> bool:
    if "#" in link:  # 指定标题
        pattern = r"^#{1,6}\s+.*$"
        if not link.startswith("#"):
            filepath = os.path.join(os.path.dirname(filepath), link.split("#")[0])  # fmt: skip
        with open(filepath, "r", encoding="utf-8") as f:
            return re.search(pattern, str(f.read()), re.MULTILINE) is not None
    else:  # 没有指定标题，仅仅是另一个文件
        for _ in range(len(link.split("/"))):
            filepath = os.path.dirname(filepath)
        anotherfile_path = os.path.join(filepath, link)
        return os.path.exists(anotherfile_path)


# 清除不需要的图片()
def clean():
    ...


if __name__ == "__main__":
    # change()
    # check()
    # clean()
    pass
