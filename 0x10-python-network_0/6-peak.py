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
    f = int(len(nums) / 2) - 1
    l = int(len(nums) / 2)
    while l < len(nums):
        if f == 0 and nums[f] > nums[f + 1]:
            return nums[f]
        elif l == len(nums) - 1 and nums[l] >= nums[l - 1]:
            return nums[l]
        elif f > 0:
            if nums[f] > nums[f + 1] and nums[f] >= nums[f - 1]:
                return nums[f]
        if nums[l] > nums[l - 1] and nums[l] >= nums[l + 1]:
            return nums[l]
        l = l + 1
        f = f - 1
    return None
