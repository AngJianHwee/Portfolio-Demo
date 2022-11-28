# -*- coding: utf-8 -*-
# @Author: Ang Jian Hwee
# @Date:   2022-11-28 02:16:20
# @Last Modified by:   Ang Jian Hwee
# @Last Modified time: 2022-11-28 10:00:04

from modules.customQueueLinkedList import FIFOQueue
from flask import Flask, render_template

app = Flask(__name__)

# Global variables
queue = FIFOQueue()
next_number = 1
now_serving = 0
status = [1, 1, 1, 1]  # 1 is online, 0 is offline, -1 is busy
current_serving = [None, None, None, None]


# Frontend
@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/customerView', methods=['GET'])
def customerView():
    global queue, next_number, now_serving, status, current_serving
    return render_template('customerView.html',
                           last_number=next_number - 1,
                           now_serving=now_serving,
                           current_serving=current_serving,
                           status=status)


@app.route('/counterManagement', methods=['GET'])
def counterManagement():
    global queue, next_number, now_serving, status, current_serving
    return render_template('counterManagement.html',
                           last_number=next_number - 1,
                           now_serving=now_serving,
                           current_serving=current_serving,
                           status=status)


# Backend
# Use post to prevent user request duplication using GET by url
@app.route('/api/takeNumber', methods=['POST'])
def takeNumber():
    global queue, next_number, now_serving, status, current_serving
    queue.enqueue(next_number)
    return_value = next_number
    next_number += 1
    return render_template(
        'redirecting.html',
        message=f'Your Number is {return_value}, \n redirect in 3 seconds...',
        redirecting_url="/customerView")


# Split Offline and Online as different URL for more friendly logging
@app.route('/api/goOffline/<counter_number>', methods=['GET'])
def goOffline(counter_number):
    global queue, next_number, now_serving, status, current_serving
    counter_number = int(counter_number)
    # check
    if status[int(counter_number)] == 0:
        return render_template(
            'redirecting.html',
            message=
            f'Counter #{counter_number + 1} is already offline, \n redirect in 3 seconds...',
            redirecting_url="/counterManagement")
    if status[int(counter_number)] == -1:
        return render_template(
            'redirecting.html',
            message=
            f'Counter #{counter_number + 1} is still serving, cannot go offline, \n redirect in 3 seconds...',
            redirecting_url="/counterManagement")
    status[int(counter_number)] = 0
    return render_template(
        'redirecting.html',
        message=
        f'Counter #{counter_number + 1} sucessfully go offline, \n redirect in 3 seconds...',
        redirecting_url="/counterManagement")


@app.route('/api/goOnline/<counter_number>', methods=['GET'])
def goOnline(counter_number):
    global queue, next_number, now_serving, status, current_serving
    counter_number = int(counter_number)
    # check
    if status[int(counter_number)] == 1:
        return render_template(
            'redirecting.html',
            message=
            f'Counter #{counter_number + 1} is already online, \n redirect in 3 seconds...',
            redirecting_url="/counterManagement")
    status[int(counter_number)] = 1
    return render_template(
        'redirecting.html',
        message=
        f'Counter #{counter_number + 1} sucessfully go online, \n redirect in 3 seconds...',
        redirecting_url="/counterManagement")


@app.route('/api/callNext/<counter_number>', methods=['GET'])
def callNext(counter_number):
    global queue, next_number, now_serving, status, current_serving
    counter_number = int(counter_number)
    if queue.size() == 0:
        return render_template(
            'redirecting.html',
            message=f'No users in queue, \n redirect in 3 seconds...',
            redirecting_url="/counterManagement")
    customer = queue.dequeue()
    current_serving[counter_number] = customer
    now_serving = max(now_serving, int(customer))
    status[counter_number] = -1
    return render_template(
        'redirecting.html',
        message=
        f'Counter #{counter_number + 1} sucessfully call next customer {customer}, \n redirect in 3 seconds...',
        redirecting_url="/counterManagement")


@app.route('/api/completeCurrent/<counter_number>', methods=['GET'])
def completeCurrent(counter_number):
    global queue, next_number, now_serving, status, current_serving
    counter_number = int(counter_number)
    customer = current_serving[counter_number]
    if status[counter_number] == 0:
        return render_template(
            'redirecting.html',
            message=
            f'Counter #{counter_number + 1} is offline, cannot complete current, \n redirect in 3 seconds...',
            redirecting_url="/counterManagement")

    if customer is None:
        return render_template(
            'redirecting.html',
            message=
            f'Counter #{counter_number + 1} has no customer, cannot complete current, \n redirect in 3 seconds...',
            redirecting_url="/counterManagement")

    current_serving[counter_number] = None
    status[counter_number] = 1
    return render_template(
        'redirecting.html',
        message=
        f'Counter #{counter_number + 1} complete customer {customer}, \n redirect in 3 seconds...',
        redirecting_url="/counterManagement")


# Reset everything
@app.route('/api/reset', methods=['GET'])
def reset():
    global queue, next_number, now_serving, status, current_serving
    queue = FIFOQueue()
    next_number = 1
    now_serving = 0
    status = [1, 1, 1, 1]  # 1 is online, 0 is offline, -1 is busy
    current_serving = [None, None, None, None]
    return "Reset success."
