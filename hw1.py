#!/usr/bin/python
__author__ = "Stephen Li"
__email__ = "stephen.liziyun at gmail dot com"

import sys

def sort_and_count(array, length):
    if len(array) != length:
        print 'The input length is not match to input array! '
        sys.exit(1)
    if length == 1:
        return 0
    else:
        left_half_array = array[ : (length/2)]
        right_half_array = array[(length/2) : ]
        x = sort_and_count(left_half_array, len(left_half_array))
        y = sort_and_count(right_half_array, len(right_half_array))
        z = merge_and_count_split_inv(sorted(left_half_array), sorted(right_half_array), length)
        return (x + y + z)

def merge_and_count_split_inv(left, right, length):
    num_inv = 0
    i = 0   # index for left half array
    j = 0   # index for right half array
    len_left = len(left)
    len_right = len(right)

    for x in xrange(0,length):
        if i < len_left and j < len_right:
            if left[i] < right[j]:
                i += 1
            elif left[i] > right[j]:
                num_inv  += len_left - i
                j += 1
    return num_inv

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
    print sort_and_count(input_array, len(input_array))
    print len(input_array)
    # Test case for merge_and_count_split_inv
    # print merge_and_count_split_inv([1, 3, 5], [2, 4, 6], 6)
    # print sort_and_count([1, 3, 5, 2, 4, 6], 6)

if __name__ == '__main__':
    main()

