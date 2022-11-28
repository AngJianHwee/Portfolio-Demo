# -*- coding: utf-8 -*-
# @Author: Ang Jian Hwee
# @Date:   2022-11-28 02:25:24
# @Last Modified by:   Ang Jian Hwee
# @Last Modified time: 2022-11-28 12:33:11

from modules import customQueueLinkedList
import pytest
from pytest import approx
import numpy as np

def test_custom_queue_linked_list_FIFO_initialize():
	q = customQueueLinkedList.FIFOQueue()
	assert q.tail is q.head
	assert q.queue_size == 0

def test_custom_queue_linked_list_FIFO_enqueue():
	q = customQueueLinkedList.FIFOQueue()
	q.enqueue(1)
	assert q.head.next_node.value == '1'
	assert q.queue_size == 1

def test_custom_queue_linked_list_FIFO_size():
	q = customQueueLinkedList.FIFOQueue()
	q.enqueue(1)
	q.enqueue("2")
	q.enqueue(3.0)
	assert q.size() == 3

def test_custom_queue_linked_list_FIFO_dequeue():
	q = customQueueLinkedList.FIFOQueue()
	q.enqueue(1)
	q.enqueue("2")
	q.enqueue(3.0)
	assert q.dequeue() == '1'
	assert q.queue_size == 2
	assert q.dequeue() == "2"
	assert q.dequeue() == "3.0"


def test_custom_queue_linked_list_FIFO_getQueue():
	q = customQueueLinkedList.FIFOQueue()
	q.enqueue(1)
	q.enqueue("2")
	q.enqueue(3.0)
	assert q.dequeue() == '1'
	assert np.array(q.getQueue()) == approx(np.array(["2",3.0]))

def test_custom_queue_linked_list_LIFO_initialize():
	q = customQueueLinkedList.FIFOQueue()
	assert q.tail is q.head
	assert q.queue_size == 0

def test_custom_queue_linked_list_LIFO_enqueue():
	q = customQueueLinkedList.LIFOQueue()
	q.enqueue(1)
	assert q.head.next_node.value == '1'
	assert q.queue_size == 1

def test_custom_queue_linked_list_LIFO_size():
	q = customQueueLinkedList.LIFOQueue()
	q.enqueue(1)
	q.enqueue("2")
	q.enqueue(3.0)
	assert q.size() == 3

def test_custom_queue_linked_list_LIFO_dequeue():
	q = customQueueLinkedList.LIFOQueue()
	q.enqueue(1)
	q.enqueue("2")
	q.enqueue(3.0)
	assert q.dequeue() == '3.0'
	assert q.queue_size == 2
	assert q.dequeue() == "2"
	assert q.dequeue() == "1"


def test_custom_queue_linked_list_LIFO_getQueue():
	q = customQueueLinkedList.LIFOQueue()
	q.enqueue(1)
	q.enqueue("2")
	q.enqueue(3.0)
	assert q.dequeue() == '3.0'
	assert np.array(q.getQueue()) == approx(np.array([1,"2"]))
