from __future__ import division
#!/usr/bin/python

__author__ = "Stephen Li"
__email__ = "stephen.liziyun at gmail dot com"


import sys
import random
import math


# define a globle counting for comparisons
count = 0

def QuickSort(array):
    length = len(array)
    if length == 0:
        return array
    elif length == 1:
        return array # no need to sort single-element array
    else:
        global count
        random.seed()   # reset random seed, may be redundant
        # pivot_idx = random.randint(0, (length-1)) # totally randomized
        pivot_idx = 0                               # always use the first element
        # pivot_idx = length-1                      # always use the last element
        # Median of 3
        # middle_idx = (int)(math.ceil(length / 2)) - 1
        # pivot_idx = array.index(Median(array[0], array[length-1], array[middle_idx]))
        pivot = array[pivot_idx]
        array, new_pivot_idx = Partition(array, pivot_idx, length)
        left = QuickSort(array[:new_pivot_idx])
        count = count + new_pivot_idx - 1
        right = QuickSort(array[new_pivot_idx+1:])
        count = count + length - new_pivot_idx
        return left + [array[new_pivot_idx]] + right

def Partition(array, pivot_idx, length):
    # swap pivot and first element, might be redundant
    array[pivot_idx], array[0] = array[0], array[pivot_idx]
    pivot = array[0]
    i = 1
    for j in xrange(i,length):
        if array[j] < pivot:
            # swap array[i] and array[j]
            array[i], array[j] = array[j], array[i]
            i = i + 1
    # swap pivot(first element) and array[i-1]
    array[0], array[i-1] = array[i-1], array[0]
    # return array and pivot's new index
    return (array, i-1)

def Median(a, b, c):
    if a > b:
        if c > b:
            return min(a, c)
        else:
            return b
    else:
        if c > a:
            return min(b, c)
        else:
            return a

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
    # print input_array
    # print len(input_array)
    print Median(1, 2, 3)
    print Median(1, 3, 2)
    print Median(2, 1, 3)
    print Median(2, 3, 1)
    print Median(3, 2, 1)
    print Median(3, 1, 2)
    sorted_array = QuickSort(input_array)
    print sorted_array
    print count

if __name__ == '__main__':
    main()