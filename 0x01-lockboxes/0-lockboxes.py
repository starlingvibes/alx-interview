#!/usr/bin/python3

"""Module 0-lockboxes.
Returns a boolean true or false if it's
possible to open all boxes or not.
"""

def canUnlockAll(boxes):
    """Returns if it's possible to open all boxes

    Args:
        - boxes: a list of lists

    Returns: true or false
    """
    arr = []
    seen = set()
    truelen = 0
    for box in boxes:
        if len(box) != 0:
            truelen += 1
    for x in range(len(boxes[0])):
        arr.append(boxes[0][x])
    for idx in arr:
        if len(boxes[idx]) == 0 or idx in seen:
            break
        seen.add(idx)
        for num in boxes[idx]:
            arr.append(num)
    return len(set(arr)) == truelen
