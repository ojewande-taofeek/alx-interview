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
    print("File size: {}".format(total))
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

for line in sys.stdin:
    status_match = re.search(r'\s\d{3}\s', line)
    file_size_match = re.search(r'\s\d{1,4}$', line)
    if status_match and file_size_match:
        status = int(status_match.group().strip())
        file_size = int(file_size_match.group().strip())
        if status in status_code and isinstance(file_size, int):
            total += file_size
            counter += 1
            if status in storage:
                val = storage.get(status)
                storage[status] = val + 1
            else:
                storage[status] = 1
            if counter % 10 == 0:
                printer()
        else:
            continue
    else:
        continue
