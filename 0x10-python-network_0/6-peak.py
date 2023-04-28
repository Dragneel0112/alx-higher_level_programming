#!/usr/bin/python3
"""
Determines the peak in an unsorted list
"""


def find_peak(list_of_integers):
    """
        Args: list_of_integers - List of unsorted ints
        Return: Peak from list
    """
    loi = list_of_integers
    if not loi:
        return None

    i = 1
    peak = loi[i]
    while i < len(loi) - 1:
        if (loi[i - 1] <= loi[i] and loi[i + 1] <= loi[i] and loi[i] > peak):
            peak = loi[i]
        i += 1
    return peak
