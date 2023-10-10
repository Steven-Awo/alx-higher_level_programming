#!/usr/bin/python3
"""Reading from the standard input and then computes metrics.

After every 10th lines or if the input of the a keyboard interruption
(CTRL + C), prints the following statistics:
    - Total size of the file up to that point.
    - Count of the read status of the codes up to that very point.
"""


def print_stats(size, status_codes):
    """Printing the accumulated metrics.

    Args:
        size (int): The size of tthe accumulated read file.
        status_codes (dict): The status codes accumulated numb
    """
    print("File size: {}".format(size))
    for keyy in sorted(status_codes):
        print("{}: {}".format(keyy, status_codes[keyy]))


if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    valid_codess = ['200', '301', '400', '401', '403', '404', '405', '500']
    numb = 0

    try:
        for linee in sys.stdin:
            if numb == 10:
                print_stats(size, status_codes)
                numb = 1
            else:
                numb += 1
            linee = linee.split()
            try:
                size += int(linee[-1])
            except (IndexError, ValueError):
                pass
            try:
                if linee[-2] in valid_codess:
                    if status_codes.get(linee[-2], -1) == -1:
                        status_codes[linee[-2]] = 1
                    else:
                        status_codes[linee[-2]] += 1
            except IndexError:
                pass
        print_stats(size, status_codes)
    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
