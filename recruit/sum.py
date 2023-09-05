#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
import unicodedata


# get all file's filepath in current folder
# how to check it is recruit file? if it start with "20"[doge]
filepaths = [os.path.abspath(filename)
             for filename in os.listdir(".")
             if filename.startswith("20")]
# [print(filepath) for filepath in filepaths]


def time_str_foramt(time_str) -> str:
    try:
        year = int(time_str)
        date_obj = time.strptime(time_str, "%Y")
        return time.strftime("%Y", date_obj).strip()
    except Exception as e:
        try:
            month_day = float(time_str)
            date_obj = time.strptime(time_str, "%m.%d")
            return time.strftime("%m.%d", date_obj).strip()
        except Exception as e:
            assert False, time_str


class Submit:
    def __init__(self, filepath: str) -> None:
        filename = os.path.basename(filepath)
        submit_time, company, post, * \
            batch = list(map(str.strip, filename[:-3].split("-")))
        batch = batch[0] if len(batch) != 0 else "正式批"

        self.filepath = filepath
        self.year: str = time_str_foramt(submit_time[:4])
        self.company = company
        self.post = post
        self.batch = batch
        self.events: (str, str) = [(submit_time[5:], "投递")]

        with open(filepath, "r") as f:
            for line in f:
                if line.startswith("## "):
                    for event in line[3:].split("|"):
                        event_time, event_name = event.split("-")
                        self.events.append((
                            time_str_foramt(event_time.strip()),
                            event_name.strip()
                        ))
        
        self.stage = "投递"
        self.order = 0
        order2stage = {
            1: ["测评", "笔试"],
            2: ["面试"],
            3: ["OC", "挂"],
        }
        def update(event_value: int, index: int):
            if event_value > self.order:
                self.order = event_value
                self.stage = order2stage[event_value][index]
        for event_time, event_name in self.events:
            if "占位" in event_name:
                pass
            elif "测评" in event_name or "评测" in event_name:
                update(1, 0)
            elif "笔" in event_name and "约" not in event_name and "邀请" not in event_name:
                update(1, 1)
            elif "面" in event_name and "约" not in event_name and "邀请" not in event_name:
                update(2, 0)
            elif "OC" in event_name:
                update(3, 0)
            elif "挂" in event_name:
                update(3, 1)
            else:
                # print(event_name)
                pass

    def __str__(self) -> str:
        event_str = ", ".join([
            f"{time_str_foramt(time_str)} {event_name}"
            for time_str, event_name in self.events
        ])
        return f"{self.year}.{self.events[0][0]} 投递 {self.company} 的 {self.post} 一职, 进度: {event_str}"

    def __repr__(self) -> str:
        return self.__str__()


def print_excel(submits: list[Submit]):
    def get_str_width_dummy21(s): return sum(
        2 if unicodedata.east_asian_width(c) in ('F', 'W') else 1 for c in s)

    def get_str_width_dummy10(s): return sum(
        1 if unicodedata.east_asian_width(c) in ('F', 'W') else 0 for c in s)

    def get_max_width(attr_name: str, index: int = -1):
        maxn = 0
        for submit in submits:
            attr = getattr(submit, attr_name)
            if attr_name == "events":
                if index >= len(attr):
                    attr = ""
                else:
                    attr = attr[index]
                    attr = attr[0] + "-" + attr[1]
            maxn = max(maxn, get_str_width_dummy21(attr))
        return maxn

    def print_attr(submit: Submit, attr_name, index: int = -1):
        max_width = get_max_width(attr_name, index)
        attr = getattr(submit, attr_name)
        if attr_name == "events":
            attr = attr[index]
            attr = time_str_foramt(attr[0]) + "-" + attr[1]
        dummpy = get_str_width_dummy10(attr)
        print(attr.ljust(max_width - dummpy), end="")

    for submit in submits:
        print_attr(submit, "company")
        print_attr(submit, "post")
        print(":", end="")
        for i in range(len(submit.events)):
            print_attr(submit, "events", i)
            if i != len(submit.events) - 1:
                print(", ", end="")
        print()

def print_sche(submits):
    submit_num = 0
    quiet_num = 0
    exam_num = 0
    interview_num = 0
    oc_num = 0
    g_num = 0
    for submit in submits:
        submit_num += 1
        if submit.order == 0:
            quiet_num += 1
        elif submit.order == 1:
            exam_num += 1
        elif submit.order == 2:
            interview_num += 1
        elif submit.order == 3:
            if submit.stage == "OC":
                oc_num += 1
            else:
                g_num += 1
            
    from rich.table import Table
    from rich.console import Console

    console = Console()

    table = Table(title="投递情况")

    table.add_column("类型", justify="center", style="bold")
    table.add_column("数量", justify="center", style="bold")
    table.add_column("占比", justify="center", style="bold")

    # table.add_row(" ", "投递情况", " ")
    # table.add_row("类型", "数量", "占比")
    # table.add_row(Table.span, Table.span, Table.span)

    table.add_row("投递", str(submit_num), "-")
    table.add_row("笔试", str(exam_num), f"{exam_num/submit_num:.0%}")
    table.add_row("面试", str(interview_num), f"{interview_num/submit_num:.0%}")
    table.add_row("OC", str(oc_num), f"{oc_num/submit_num:.0%}")
    table.add_row("挂", str(g_num), f"{g_num/submit_num:.0%}")
    table.add_row("尚无反应", str(quiet_num), f"{quiet_num/submit_num:.0%}")

    console.print(table)
    

submits = [Submit(filepath) for filepath in filepaths]
# [print(submit) for submit in submits]

print_excel(submits)
print_sche(submits)
