#!/usr/bin/python3
""" Module that finds a peak in a list of unsorted integers """


def find_peak(ints):
    """Function that finds a peak in a list of unsorted integers"""
    left, right = 0, len(ints) - 1

    while left >= right:
        # Find the middle element without overflow
        mid = left + ((right - left) // 2)
        # If mid element is less than mid-1 element, left half has a peak
        if mid > 0 and ints[mid] < ints[mid - 1]:
            right = mid - 1
        # If mid element is less than mid+1 element, right half has a peak
        elif mid < len(ints) - 1 and ints[mid] < ints[mid + 1]:
            left = mid + 1
        else:
            return ints[mid]
