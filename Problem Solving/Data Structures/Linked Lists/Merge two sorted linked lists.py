#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(head1, head2):
    # # Solution 1: Using helper function
    # def merge(p1, p2, insert_node):
    #     head = insert_node
    #     while True:
    #         if p2 is None:
    #             return head
    #         elif p1 is None:
    #             insert_node.next = p2
    #             return head

    #         if p1.data <= p2.data:
    #             p1 = p1.next
    #             insert_node = insert_node.next
    #         else:
    #             tmp = p2.next
    #             insert_node.next = p2
    #             p2.next = p1
    #             insert_node = insert_node.next
    #             p2 = tmp

    # if head1 is None:
    #     return head2
    # if head2 is None:
    #     return head1

    # flag = True if head1.data <= head2.data else False

    # if flag:
    #     p1, p2, tmp = head1.next, head2, head1
    #     return merge(p1, p2, tmp)
    # else:
    #     p1, p2, tmp = head1, head2.next, head2
    #     return merge(p2, p1, tmp)

    # Solution 2
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    # Find the minimum node
    if head1.data <= head2.data:
        out_head = head1
        head1 = head1.next
    else:
        out_head = head2
        head2 = head2.next

    tmp = out_head
    while True:
        if head1 is None:
            tmp.next = head2
            break
        if head2 is None:
            tmp.next = head1
            break

        if head1.data <= head2.data:
            min_node = head1
            head1 = head1.next
        else:
            min_node = head2
            head2 = head2.next

        tmp.next = min_node
        tmp = tmp.next

    return out_head




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)
            
        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        llist3 = mergeLists(llist1.head, llist2.head)

        print_singly_linked_list(llist3, ' ', fptr)
        fptr.write('\n')

    fptr.close()

