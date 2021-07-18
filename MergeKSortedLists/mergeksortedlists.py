"""
Given an array of ‘K’ sorted LinkedLists, merge them into one sorted list.
"""

from heapq import *
class List():
    def __init__(self, value):
        self.value = value
        self.next = None


def mergeK(input_lists):
    minheap = []
    for root_node in input_lists:
        heappush(minheap, root_node)
    result_head , result_tail = None, None
    while minheap:
        node = heappop(minheap)
        if result_head is None:
            result_head, result_tail = node
        else:
            result_tail.next = node
            result_tail = result_tail.next

        if node is not None:
            heappush(minheap, node.next)
    return result_head



