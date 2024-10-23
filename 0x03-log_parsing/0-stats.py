#!/usr/bin/python3
"""
    script that reads stdin line by line and computes metrics
"""
import re
import sys
import signal


total = 0
counter = 0
status_code = [200, 301, 400, 401, 403, 404, 405, 500]
storage = dict()


def printer():
    """
        Prints the output
    """
    print("File size: {:d}".format(total))
    for key, value in sorted(storage.items()):
        print("{}: {}".format(key, value))


def handler(signum, frame):
    """
        The signal handler
    Args:
        signum (int): The signal number
        frame (Object): The stack frame object
    """
    printer()
    sys.exit(0)


signal.signal(signal.SIGINT, handler)
pattern = (
    r"^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - "
    r"\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6})\] "
    r'"GET /projects/\d+ HTTP/1\.1" '
    r"(\d{3}) "
    r"(\d+)$"
)


for line in sys.stdin:
    match = re.match(pattern, line)
    if match:
        # print(line)
        status_match = match.group(3)
        file_size_match = match.group(4)
        if status_match and file_size_match:
            status = int(status_match)
            file_size = int(file_size_match)
            if status in status_code and isinstance(file_size, int):
                total += file_size
                counter += 1
                if status in storage:
                    val = storage.get(status)
                    storage[status] = val + 1
                else:
                    storage[status] = 1
                if counter % 10 == 0 and counter != 0:
                    printer()
            else:
                continue
        else:
            continue
