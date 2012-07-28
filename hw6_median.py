from __future__ import division
#!/usr/bin/python
__author__ = "Stephen Li"
__email__ = "stephen.liziyun at gmail dot com"

import sys
from heapq import heappush, heappop
from math import floor

def MedianMaintainance(heap_high, heap_low, item):
    # Heap push
    if len(heap_high) == 0:
        heappush(heap_high, item)
        return heap_high[0]
    if item > heap_high[0]: # heap[0] is the smallest element
        heappush(heap_high, item)
    else:
        heappush(heap_low, -item)
    # Balance if needed
    dif = len(heap_high) - len(heap_low)
    if dif > 1:
        for i in xrange(0, int(floor(dif/2))):
            temp = heappop(heap_high)
            heappush(heap_low, -temp)
    if dif < -1:
        for i in xrange(0, -int(floor(dif/2))):
            temp = heappop(heap_low)
            heappush(heap_high, -temp)
    # Calculate median
    dif = len(heap_high) - len(heap_low)
    median = 0
    if dif == 0:
        # median = (heap_high[0] - heap_low[0]) / 2 # Too good for this homework
        median = -heap_low[0]
    elif dif == 1:
        median = heap_high[0]
    elif dif == -1:
        median = -heap_low[0]
    else:
        print 'Error: Heaps are not as balanced as possible'
        sys.exit(1)

    return int(median)


def main():
    args = sys.argv[1:]
    if not args:
        print 'usage: inputfile'
        sys.exit(1)

    heap_high = []
    heap_low = []
    median_sum = 0
    median_list = []
    with open(args[0]) as fileobject:
        for line in fileobject:
            num = int(line.strip().split()[0])
            median = MedianMaintainance(heap_high, heap_low, num)
            median_sum += median
            median_list.append(median)

    # print heap_high
    # print heap_low
    # print len(heap_high) - len(heap_low)
    print median_list
    print 'Median Sum:', median_sum
    print 'Result', median_sum % 10000

if __name__ == '__main__':
    main()