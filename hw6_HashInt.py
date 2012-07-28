#!/usr/bin/python
__author__ = "Stephen Li"
__email__ = "stephen.liziyun at gmail dot com"

import sys

def CountTwoSum(input_hash, interval):
    x_array = input_hash.keys()
    counter = 0
    for t in interval:
        # t_count = 0
        for x in x_array:
            if (input_hash.has_key(t-x)) and (x != t-x):
                counter += 1
                break
    return counter

def main():
    args = sys.argv[1:]
    if not args:
        print 'usage: inputfile'
        sys.exit(1)

    input_hash = {}
    with open(args[0]) as fileobject:
        for line in fileobject:
            key = line.strip().split() # key is a list
            input_hash[int(key[0])] = True

    # Test output
    # for key in input_hash.keys():
    #     if key >= 2500 and key <= 4000:
    #         print key, input_hash[key]

    counter = CountTwoSum(input_hash, range(2500, 4000+1))
    print counter # 1477

if __name__ == '__main__':
    main()