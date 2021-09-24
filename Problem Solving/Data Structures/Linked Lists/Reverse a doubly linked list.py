#!/bin/python3

import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

#
# Complete the 'reverse' function below.
#
# The function is expected to return an INTEGER_DOUBLY_LINKED_LIST.
# The function accepts INTEGER_DOUBLY_LINKED_LIST llist as parameter.
#

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#

def reverse(llist):
    # 0-node, 1-node llist
    if llist is None or llist.next is None:
        return llist
    # 2-node llist
    if llist.next.next is None:
        first = llist
        last = llist.next
        first.next = None
        first.prev = last
        last.next = first
        last.prev = None
        return last
    # More than 2-node llist
    first = llist
    # Get the last node
    last = llist
    while last.next is not None:
        last = last.next
    # Reversing
    while True:
        # Reverse the first and last
        prev_first = first.prev
        next_first = first.next
        next_last = last.next
        prev_last = last.prev
        
        last.next = next_first
        last.prev = prev_first
        prev_last.next = first
        if next_last:
            next_last.prev = first
        
        first.next = next_last
        first.prev = prev_last
        next_first.prev = last
        if prev_first:
            prev_first.next = last
        # Assign new values to first and last
        first = next_first
        last = prev_last
        # Check for exiting criterion
        if (first is last):  # Odd number of nodes
            break
        if first.next is last: # Even number of nodes
            prev_first = first.prev
            next_first = first.next
            next_last = last.next
            prev_last = last.prev
            
            last.next = first
            last.prev = prev_first
            first.next = next_last
            first.prev = last
            prev_first.next = last
            next_last.prev = first
            break
    # Get the head
    tmp = llist
    while tmp.prev is not None:
        tmp = tmp.prev
    return tmp
    

    
    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        llist1 = reverse(llist.head)

        print_doubly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')

    fptr.close()

