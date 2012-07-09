#!/usr/bin/python
__author__ = "Stephen Li"
__email__ = "stephen.liziyun at gmail dot com"

import sys

def main():
    args = sys.argv[1:]
    if not args:
        print 'usage: inputfile'
        sys.exit(1)

    input_array= []
    f = open(args[0])
    for line in f:
        new_num = int(line)
        input_array.append(new_num)
    f.close
    print input_array
    print len(input_array)

if __name__ == '__main__':
    main()