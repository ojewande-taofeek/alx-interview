#!/usr/bin/python3
"""
    script that reads stdin line by line and computes metrics
"""
import re
import sys


total = 0
counter = 0
status_code = [200, 301, 400, 401, 403, 404, 405, 500]
storage = dict()


def printer():
    """
        Prints the output
    """
    print("File size: {:d}".format(total))
    for key in sorted(storage.keys()):
        print("{}: {:d}".format(key, storage[key]))


# def handler(signum, frame):
    """
        The signal handler
    Args:
        signum (int): The signal number
        frame (Object): The stack frame object
    """
# printer()


# signal.signal(signal.SIGINT, handler)
pattern = re.compile(
    r"^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - "
    r"\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6})\] "
    r'"GET /projects/\d+ HTTP/1\.1" '
    r"(\d{3}) "
    r"(\d+)$"
)


try:
    for line in sys.stdin:
        match = pattern.match(line)
        if match:
            status = match.group(3)
            file_size = int(match.group(4))
            total += file_size
            counter += 1
            if int(status) in status_code:
                storage[status] = storage.get(status, 0) + 1
            if counter % 10 == 0:
                printer()
        else:
            try:
                line_split = line.split()
                file_size = int(line_split[-1])
                if file_size:
                    total += file_size
            except (IndexError, TypeError, ValueError):
                pass
    if counter % 10 != 0 or counter == 0:
        printer()
except KeyboardInterrupt:
    printer()
    raise
