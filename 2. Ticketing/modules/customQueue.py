# -*- coding: utf-8 -*-
# @Author: Ang Jian Hwee
# @Date:   2022-11-28 02:20:08
# @Last Modified by:   Ang Jian Hwee
# @Last Modified time: 2022-11-28 09:59:31


class FIFOQueue(object):
    def __init__(self):
        self.array = []
        self.queue_size = 0

    def enqueue(self, value):
        self.array.append(str(value))
        self.queue_size += 1
        return self.array

    def size(self):
        return self.queue_size

    def dequeue(self):
        if self.queue_size == 0:
            return None
        else:
            return_value = self.array[0]

            if self.queue_size == 1:
                self.array = []

            else:
                self.array = self.array[1:]

            self.queue_size -= 1
            return return_value

    def getQueue(self):
        return self.array


class LIFOQueue(object):
    def __init__(self):
        self.array = []
        self.queue_size = 0

    def enqueue(self, value):
        self.array.append(str(value))
        self.queue_size += 1
        return self.array

    def size(self):
        return self.queue_size

    def dequeue(self):
        if self.queue_size == 0:
            return None
        else:
            if self.queue_size == 1:
                return_value = self.array[0]
                self.array = []

            else:
                return_value = self.array[-1]
                self.array = self.array[:-1]

            self.queue_size -= 1
            return return_value

    def getQueue(self):
        return self.array
