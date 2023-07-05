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
# Complete the 'sortedInsert' function below.
#
# The function is expected to return an INTEGER_DOUBLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_DOUBLY_LINKED_LIST llist
#  2. INTEGER data
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

def sortedInsert(llist, data):
    new_node = DoublyLinkedListNode(data)
    # Check for empty llist
    if not llist:
        return new_node

    is_last_node = False
    tmp = llist
    while tmp.data <= new_node.data:
        if tmp.next is None:
            is_last_node = True
            break
        tmp = tmp.next

    if is_last_node:
        tmp.next = new_node
        new_node.prev = tmp
        return llist

    if tmp is llist:
        new_node.next = llist
        llist.prev = new_node
        return new_node

    prev_node = tmp.prev
    prev_node.next = new_node
    new_node.next = tmp
    tmp.prev = new_node
    new_node.prev = prev_node

    return llist

    # # Old Solution
    # # Check for one node llist
    # if llist.data >= data:
    #     new_node.next = llist
    #     llist.prev = new_node
    #     return new_node

    # # Finding the right node
    # tmp = llist
    # while True:
    #     if not tmp.next:
    #         tmp.next = new_node
    #         new_node.prev = tmp
    #         return llist
    #     current_data = tmp.data
    #     next_data = tmp.next.data
    #     if current_data <= data <= next_data:
    #         break
    #     tmp = tmp.next

    # # Inserting the node
    # p1 = tmp
    # p2 = tmp.next
    # p1.next = new_node
    # new_node.next = p2
    # p2.prev = new_node
    # new_node.prev = p1

    # return llist


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        data = int(input())

        llist1 = sortedInsert(llist.head, data)

        print_doubly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')

    fptr.close()

