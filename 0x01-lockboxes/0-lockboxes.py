#!/usr/bin/python3
""" Module for the connected graph algorithm
"""
from queue import Queue


def canUnlockAll(boxes):
    """ Check if an adjacency list represented graph is connected
    """
    if not boxes:
        return True

    slots = [False] * len(boxes)
    q = Queue(len(boxes))

    slots[0] = True
    for key in boxes[0]:
        if key < len(boxes):
            slots[key] = True
            q.put(key)

    while not q.empty():
        for key in boxes[q.get()]:
            if key < len(boxes) and not slots[key]:
                slots[key] = True
                q.put(key)

    return all(slots)
