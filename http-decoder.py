#!/usr/bin/python
import html
import argparse
import os


def build_cli():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help='String to decode')
    parser.add_argument('-f', '--file', help='File containing strings to decode')
    args = parser.parse_args()

    if args.input and args.file:
        raise RuntimeError('You can\'t use both <input> and <file> options!')
    elif not (args.input or args.file):
        raise RuntimeError('Please use either the <input> or <file> option!')
    return args


def useFile(filename):
    if not os.path.exists(filename):
        raise RuntimeError('%s does not exist! Pick a different file!' % filename)
    print('')
    print('Decoded:')
    with open(filename, 'r') as ifile:
        for line in ifile:
            print('\t'+html.unescape(line))
    print('')


def useInput(encoded):
    print('')
    print('Decoded:')
    print('\t'+html.unescape(encoded))
    print('')


if __name__ == '__main__':
    print("""
    ==============================
    |   Welcome to HTML Decoder  |
    ==============================
    """)
    args = build_cli()
    if args.file:
        useFile(args.file)
    elif args.input:
        useInput(args.input)
