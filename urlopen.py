#! /usr/bin/env python3

import webbrowser
import re
from pathlib import Path


def main():
    if args.url != '':
        webbrowser.open(args.url)
        return

    if args.file != '':
        if args.file.startswith('/'):
            # absolute path
            pass
        else:
            # relative path
            path = Path(__file__)
            filepath = path.parent.resolve() / args.file
            url_list = find_urls(filepath)
            print(url_list)


def find_urls(file):
    # Find URLs from a text file
    # and returns list
    text_data = open(file, 'r')
    content = text_data.read()

    pattern = re.compile('https?:\/\/[-_.!~*\'a-zA-Z0-9;\/?:\@&=+\$,%#]+')
    return pattern.findall(content)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(
        description='Open specified URL web page by a browser.'
    )
    parser.add_argument(
        '-u',
        '--url',
        help='URL to open',
        default='',
        type=str
    )
    parser.add_argument(
        '-f',
        '--file',
        help='Choose text file that contains URLs. \
        The urlopen finds URLs and open them by a browser.',
        default='',
        type=str
    )
    args = parser.parse_args()

    main()
