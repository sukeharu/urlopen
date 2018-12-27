#! /usr/bin/env python3

import webbrowser
import re
import tkinter as tk
from tkinter import filedialog
from pathlib import Path


def main():
    if args.url != '':
        webbrowser.open(args.url)
        return

    filepath = ''
    if args.dialog:
        root = tk.Tk()
        root.withdraw()
        filepath = filedialog.askopenfilename(title='Choose Text file.')
    else:
        if args.file != '':
            if args.file.startswith('/'):
                # absolute path
                filepath = args.file
            else:
                # relative path
                path = Path(__file__)
                filepath = path.parent.resolve() / args.file

    if filepath != '':
        try:
            url_list = find_urls(filepath)
            if len(url_list) == 0:
                print('URL Not found in the file.')
            else:
                for page in url_list:
                    webbrowser.open(page)
        except UnicodeDecodeError as e:
            print('Choose UTF-8 encoded text file! Error: {}'.format(e))


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
        '-d',
        '--dialog',
        help='Open file dialog. -d and -f options can\'t be specified at the same time.\
        If both are specified, \
        file dialog will be open (-d option will be used).',
        action='store_true'
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
