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
    for i in range(0, len(nums)):
        if i > 0 and i < len(nums) - 1:
            if nums[i - 1] <= nums[i] and nums[i + 1] <= nums[i]:
                return nums[i]
        if i == 0 and nums[i + 1] <= nums[i]:
            return nums[i]
        if i == len(nums) - 1 and nums[i - 1] <= nums[i]:
            return nums[i]
    return None
