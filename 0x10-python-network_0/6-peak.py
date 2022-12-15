#!/usr/bin/python3
"""
This file contains a function that finds the peak
"""

def find_peak(list_of_integers):
    """
    This function finds the peak value in the array
    """
    if len(list_of_integers) == 0:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    nums = list_of_integers
    last_index= len(nums) - 1
    i = 0
    max = nums[i]
    while i <= last_index:
        if i == last_index and nums[i] > max:
            max = nums[i]
        elif nums[i] >= nums[last_index] and nums[i] >= max:
            max = nums[i]
        elif nums[i] < nums[last_index] and nums[last_index] >= max:
            max = nums[last_index]
        i = i + 1
        last_index = last_index - 1
    return max
