import os

filepaths = [os.path.abspath(os.path.join(dirpath, filename))
    for dirpath, dirnames, filenames in os.walk(".")
    for filename in filenames
    if filename.startswith("20")  # ...
]

def handle(filepath: str):
    event_table = dict()
    filename = os.path.basename(filepath)
    filename_split = filename[:-3].split("-")
    event_table[filename_split[0]] = "投递"
    event_table["company"] = filename_split[1]
    event_table["post"] = filename_split[2]
    if len(filename_split) == 4:
        assert filename_split[3].strip() == "提前批", filename_split[3]
        event_table["batch"] = "提前批"
    else:
        event_table["batch"] = "正式批"

    events = list()
    with open(filepath, "r") as f:
        for line in f:
            if line.startswith("## "):
                events.append(line[3:].strip())
    for event in events:
        for section in event.split("|"):
            section_split = section.split("-")
            event_table[section_split[0]] = section_split[1]
    print(event_table)
    return event_table

for filepath in filepaths:
    print(filepath)
    handle(filepath)
