#! /usr/bin/env python3

import webbrowser


def main():
    webbrowser.open(args.url)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(
        description='Open specified URL web page by a browser.'
    )
    parser.add_argument(
        'url',
        help='URL to open',
        type=str
    )
    args = parser.parse_args()

    main()
