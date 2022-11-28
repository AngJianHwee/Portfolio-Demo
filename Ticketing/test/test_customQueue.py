# -*- coding: utf-8 -*-
# @Author: Ang Jian Hwee
# @Date:   2022-11-28 02:25:24
# @Last Modified by:   Ang Jian Hwee
# @Last Modified time: 2022-11-28 10:45:11

from modules import customQueue
import pytest
from pytest import approx
import numpy as np

def test_custom_queue_FIFO_initialize():
	q = customQueue.FIFOQueue()
	assert q.array == []
	assert q.queue_size == 0

def test_custom_queue_FIFO_enqueue():
	q = customQueue.FIFOQueue()
	q.enqueue(1)
	q.enqueue("2")
	q.enqueue(3.0)
	assert np.array(q.array) == approx(np.array([1,"2",3.0]))
	assert q.queue_size == 3

def test_custom_queue_FIFO_size():
	q = customQueue.FIFOQueue()
	q.enqueue(1)
	q.enqueue("2")
	q.enqueue(3.0)
	assert q.size() == 3

def test_custom_queue_FIFO_dequeue():
	q = customQueue.FIFOQueue()
	q.enqueue(1)
	q.enqueue("2")
	q.enqueue(3.0)
	assert q.dequeue() == '1'
	assert np.array(q.array) == approx(np.array(["2",3.0]))
	assert q.queue_size == 2
	assert q.dequeue() == "2"
	assert q.dequeue() == "3.0"


def test_custom_queue_FIFO_getQueue():
	q = customQueue.FIFOQueue()
	q.enqueue(1)
	q.enqueue("2")
	q.enqueue(3.0)
	assert q.dequeue() == '1'
	assert np.array(q.getQueue()) == approx(np.array(["2",3.0]))

def test_custom_queue_LIFO_initialize():
	q = customQueue.LIFOQueue()
	assert q.array == []
	assert q.queue_size == 0

def test_custom_queue_LIFO_enqueue():
	q = customQueue.LIFOQueue()
	q.enqueue(1)
	q.enqueue("2")
	q.enqueue(3.0)
	assert np.array(q.array) == approx(np.array([1,"2",3.0]))
	assert q.queue_size == 3

def test_custom_queue_LIFO_size():
	q = customQueue.LIFOQueue()
	q.enqueue(1)
	q.enqueue("2")
	q.enqueue(3.0)
	assert q.size() == 3

def test_custom_queue_LIFO_dequeue():
	q = customQueue.LIFOQueue()
	q.enqueue(1)
	q.enqueue("2")
	q.enqueue(3.0)
	assert q.dequeue() == '3.0'
	assert np.array(q.array) == approx(np.array([1, "2"]))
	assert q.queue_size == 2
	assert q.dequeue() == "2"
	assert q.dequeue() == "1"


def test_custom_queue_LIFO_getQueue():
	q = customQueue.LIFOQueue()
	q.enqueue(1)
	q.enqueue("2")
	q.enqueue(3.0)
	assert q.dequeue() == '3.0'
	assert np.array(q.getQueue()) == approx(np.array([1,"2"]))
