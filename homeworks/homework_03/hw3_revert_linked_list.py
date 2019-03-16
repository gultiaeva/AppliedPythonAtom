#!/usr/bin/env python
# coding: utf-8


def revert_linked_list(head):
    """
    A -> B -> C should become: C -> B -> A
    :param head: LLNode
    :return: new_head: LLNode
    """
    node = head
    if node is None:
        return None

    prev = None
    curr = head
    nex = head.next_node
    while curr:
        curr.next_node = prev
        prev = curr
        curr = nex
        if nex:
            nex = nex.next_node
    return prev
