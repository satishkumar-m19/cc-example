# example of program that calculates the median number of unique words per tweet.
#!/usr/bin/python

# Program which provides the running median, here we have used the concept of heaps.
# maintain the first half of the stream in max heap and the 2nd half in the min heap
# based on the count of the heap elements return the appropriate elements.
# Author: Satishkumar Masilamani
# Created: July 10, 2015

import heapq as hq
import random


def running_median(first_half_max_heap, second_half_min_heap, current_item):
    diff = len(first_half_max_heap) - len(second_half_min_heap)
    if diff == 0:
        if second_half_min_heap[0] <= current_item:
            hq.heappush(second_half_min_heap, current_item)
            return float(second_half_min_heap[0])
        else:
            hq.heappush(first_half_max_heap, -current_item)
            return float(-first_half_max_heap[0])
    elif diff > 0:
        if second_half_min_heap[0] <= current_item:
            hq.heappush(second_half_min_heap, current_item)
        else:
            temp_pop = hq.heappushpop(first_half_max_heap, -current_item)
            hq.heappush(second_half_min_heap, -temp_pop)
        return float((second_half_min_heap[0] - first_half_max_heap[0])/2)
    else:
        if second_half_min_heap[0] <= current_item:
            temp_pop = hq.heappushpop(second_half_min_heap, current_item)
            hq.heappush(first_half_max_heap, -temp_pop)
        else:
            hq.heappush(first_half_max_heap, -current_item)
        return float((second_half_min_heap[0] - first_half_max_heap[0])/2)


def main():
    list_of_numbers = [random.randint(0, 100) for i in range(100)]
    first_half_max_heap = []
    second_half_min_heap = []
    hq.heappush(second_half_min_heap, 25)
    print 'running median for the list of random 100 numbers : ', list_of_numbers
    print 25
    for each in list_of_numbers:
        print running_median(first_half_max_heap, second_half_min_heap, each)

if __name__ == '__main__':
    main()
