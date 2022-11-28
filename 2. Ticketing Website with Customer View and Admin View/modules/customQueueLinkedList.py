# -*- coding: utf-8 -*-
# @Author: Ang Jian Hwee
# @Date:   2022-11-28 02:20:13
# @Last Modified by:   Ang Jian Hwee
# @Last Modified time: 2022-11-28 09:59:46


class node:
    def __init__(self, value, next_node=None, previous_node=None):
        self.next_node = next_node
        self.previous_node = previous_node
        self.value = str(value)


class FIFOQueue:
    def __init__(self):
        self.head = node(None)
        self.tail = self.head
        self.queue_size = 0

    def getQueue(self):
        return_queue = []
        pointer = self.head.next_node
        while pointer is not None:
            return_queue.append(pointer.value)
            pointer = pointer.next_node
        return return_queue

    def enqueue(self, value):
        if self.tail is self.head:
            target = self.head
        else:
            target = self.tail
        target.next_node = node(value, None, self.head)
        target.next_node.previous_node = target
        self.tail = target.next_node
        self.queue_size += 1
        return self.getQueue()

    def size(self):
        return self.queue_size

    def dequeue(self):
        if self.tail is self.head:
            target = self.head
            return None
        else:
            if self.queue_size == 1:
                target = self.head.next_node
                self.head.next_node = None
                self.tail = self.head
            else:
                target = self.head.next_node
                self.head.next_node = target.next_node
                target.next_node.previous_node = self.head
            return_value = target.value
            del (target)
            self.queue_size -= 1
            return return_value


class LIFOQueue:
    def __init__(self):
        self.head = node(None)
        self.tail = self.head
        self.queue_size = 0

    def getQueue(self):
        return_queue = []
        pointer = self.head.next_node
        while pointer is not None:
            return_queue.append(pointer.value)
            pointer = pointer.next_node
        return return_queue

    def enqueue(self, value):
        if self.tail is self.head:
            target = self.head
        else:
            target = self.tail
        target.next_node = node(value, None, self.head)
        target.next_node.previous_node = target
        self.tail = target.next_node
        self.queue_size += 1
        return self.getQueue()

    def size(self):
        return self.queue_size

    def dequeue(self):
        if self.tail is self.head:
            target = self.head
            return None
        else:
            target = self.tail.previous_node
            target.next_node = None
            self.queue_size -= 1
            return_value = self.tail.value
            del (self.tail)
            self.tail = target
            return return_value
