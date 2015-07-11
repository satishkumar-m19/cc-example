# example of program that calculates the total number of times each word has been tweeted.
#!/usr/bin/python

# Program which counts the number of words occured in the stream of tweets.
# Author: Satishkumar Masilamani
# Created: July 10, 2015

from pandas import Series
from collections import Counter
import median_unique
import os
import sys


def write_count_file(wordcount_series, count_filepath):
    '''Function to write the word count'''
    f_write = open(count_filepath, 'w')
    f_write.write(wordcount_series.to_string())
    f_write.close()


def write_median_file(stream_of_median, median_filepath):
    '''Function to write the Median file'''
    f_write = open(median_filepath, 'w')
    for each in stream_of_median:
        f_write.write(repr(each) + '\n')
    f_write.close()


def main(tweets_filepath, count_filepath, median_filepath):
    ''' Function to read the file and construct word counter '''
    f_read = open(tweets_filepath, 'r')
    wordcount_series = Series()
    stream_of_median = []
    first_half_max_heap = []
    second_half_min_heap = []
    first_element_median_flag = False
    for each in f_read:
        word_counter = Counter(each.lower().rstrip().split(' '))
        word_series = Series(word_counter)
        wordcount_series = wordcount_series.add(word_series, fill_value=0)
        if first_element_median_flag:
            curr_median = median_unique.running_median(first_half_max_heap, second_half_min_heap, float(len(word_counter.keys())))
            stream_of_median.append(curr_median)
        else:
            first_element_median_flag = True
            curr_median = len(word_counter.keys())
            second_half_min_heap.append(curr_median)
            stream_of_median.append(curr_median)
    f_read.close()
    write_count_file(wordcount_series, count_filepath)
    write_median_file(stream_of_median, median_filepath)


if __name__ == '__main__':
    if len(sys.argv) == 4:
        tweets_filepath = os.path.abspath(sys.argv[1])
        count_filepath = os.path.abspath(sys.argv[2])
        median_filepath = os.path.abspath(sys.argv[3])
        main(tweets_filepath, count_filepath, median_filepath)
    else:
        main()
