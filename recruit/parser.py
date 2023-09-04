#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, time

# get all file's filepath in current folder
# how to check it is recruit file? if it start with "20"[doge]
filepaths = [os.path.abspath(os.path.join(dirpath, filename))
    for dirpath, dirnames, filenames in os.walk(".")
    for filename in filenames
    if filename.startswith("20")  # ...
]

class Submit:
    def __init__(self, year: int, company: str, post: str, batch: str) -> None:
        self.year = time.strptime(year.strip(), "%Y")
        self.company = company.strip()
        self.post = post.strip()
        self.batch = batch.strip()
        self.events = list()
    
    def add_event(self, time_str: str, event: str):
        self.events.append((time.strptime(time_str.strip(), "%m.%d"), event.strip()))
        
    def __str__(self) -> str:
        events_str = ", ".join([f"({time.strftime('%m.%d', t)}, {e})" for t, e in self.events])
        return f"Submit(year: {str(self.year.tm_year)}, company: {self.company}, post: {self.post}, batch: {self.batch}, events: [{events_str}])"
    

# parse file with filepath, return a list of time-event pairs
def parse(filepath: str) -> Submit:
    filename = os.path.basename(filepath)
    time.strptime
    # parse file name
    submit_time, company, post, *batch = list(map(str.strip, filename[:-3].split("-")))
    batch = batch[0] if len(batch) != 0 else "正式批"
    
    submit = Submit(submit_time[:4], company, post, batch)
    submit.add_event(submit_time[5:], "投递")
    
    with open(filepath, "r") as f:
        for line in f:
            if line.startswith("## "):
                for event in line[3:].split("|"):
                    event_time, event_name = event.split("-")
                    submit.add_event(event_time, event_name)
    return submit

submit_num = len(filepaths)
evaluation_num = 0
exam_num = 0
interview_num = 0
oc_num = 0
g_num = 0
no_action_num = 0

# print(f"{submit_num} have been delivered")
for filepath in filepaths:
    # print(filepath)
    submit = parse(filepath)
    # print(submit)
    
    for event in submit.events:
        event_name = event[1]
        if "测评" in event_name:
            evaluation_num += 1
        elif "笔" in event_name and "约" not in event_name:
            exam_num += 1
        elif "面" in event_name and "约" not in event_name and "邀请" not in event_name:
            interview_num += 1
        elif "oc" in event_name:
            oc_num += 1
        elif "挂" in event_name:
            g_num += 1
    if len(submit.events) == 1: # 只有投递
        no_action_num += 1

# ---

from rich.table import Table
from rich.console import Console

console = Console()

table = Table(title="投递情况")

table.add_column("类型", justify="center")
table.add_column("数量", justify="center")
table.add_column("占比", justify="center")

table.add_row("投递", str(submit_num), "-")
table.add_row("测评", str(evaluation_num), f"{evaluation_num/submit_num:.0%}")
table.add_row("笔试", str(exam_num), f"{exam_num/submit_num:.0%}")
table.add_row("面试", str(interview_num), f"{interview_num/submit_num:.0%}")
# table.add_row("OC", str(oc_num), f"{oc_num/submit_num:.0%}")
table.add_row("挂", str(g_num), f"{g_num/submit_num:.0%}")
table.add_row("尚无反应", str(no_action_num), f"{no_action_num/submit_num:.0%}")

console.print(table)

    