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
        slots[key] = True
        q.put(key)

    while not q.empty():
        opening_key = q.get()
        if opening_key < len(boxes):
            for key in boxes[opening_key]:
                if not slots[key]:
                    slots[key] = True
                    q.put(key)

    return all(slots)
