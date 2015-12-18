#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
2009 - 2013 Manuel E. Gutierrez <dhunterkde@gmail.com>
"""

import sys
import argparse
from core.shakespeare import Shakespeare
from core.colors import colorize, Color



def cli_parser():
    '''CLI Arguments Parser helper function'''
    parser = argparse.ArgumentParser(description='Process word to search.')
    parser.add_argument('-r', '--reverse', dest='reverse',
                        action='store_const',
                        const=True, default=False,
                        help='Spanish to English')
    parser.add_argument('word', metavar='word', type=str, nargs='+',
                         help='word to search')
    return parser.parse_args()

def term_printer(result, reverse):
    color1, color2 = (Color.green, Color.red)
    if reverse:
        color1, color2 = color2, color1
    for word1, word2 in result:
        print(u"{:20} : {}".format(colorize(word1, color1), colorize(word2, color2)))


def main():
    ''' Shakespeare CLI Main function '''
    args = cli_parser()
    word = unicode(" ".join(args.word), 'utf-8')
    engine = Shakespeare()
    result = engine.search(word, reverse=args.reverse)
    if result:
        term_printer(result, args.reverse)
        return 0
    else:
        # inverted search for usability
        rev = not args.reverse
        invert_result = engine.search(word, reverse=rev)
        if invert_result:
            print(colorize('No results for original search. Reversing.',
             Color.navy))
            term_printer(invert_result, reverse=rev)
            return 0
        else:
            print(u"Not found: " + colorize("\"%s\"" % word, Color.yellow))
            return 1


if __name__ == '__main__':
    sys.exit(main())
