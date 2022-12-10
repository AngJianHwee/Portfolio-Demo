# -*- coding: utf-8 -*-
# @Author: Ang Jian Hwee
# @Date:   2022-09-19 22:58:23
# @Last Modified by:   Ang Jian Hwee
# @Last Modified time: 2022-12-10 11:24:03


from flask import Flask, render_template_string, request, redirect, render_template
import redis

try:
    r = redis.Redis("redis-269b983e-spacehotline-c3fa.aivencloud.com",22352, 0, 'AVNS_5OPWSuYPF7QPibRVAh5')
    r.ping()
except:
    r = redis.Redis("redis-10701.c62.us-east-1-4.ec2.cloud.redislabs.com",10701, 0, 'G5geqLgrwhoY569qaXYWcX6oNCHdFWht')
    r.ping()

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/newMessage', methods=["POST", "GET"])
def newMessage():
    if request.method == 'GET':
        return redirect("/")

    if r.get("cur_increment") is None:
        r.set("cur_increment", 1)

    cur_increment = int(r.get("cur_increment").decode('UTF-8'))
    content = request.form['content']

    r.setex(f'A{cur_increment:04d}', request.form['expiredInSeconds'], content)

    new_string = f'''
        Your link is <a href = "/message/A{cur_increment:04d}">{request.host_url[:-1]}/message/A{cur_increment:04d}</a>
        <br><hr>
        Expired in {request.form['expiredInSeconds']} seconds.
        <br><hr>
        <textarea rows="15" cols="60" required>{content}</textarea>
        '''

    r.incr("cur_increment")

    return render_template_string(new_string)


@app.route('/message/<key>', methods=["GET"])
def message(key):
    # return render_template_string(message_dict[key])
    try:
        return render_template_string(f'<textarea rows="15" cols="60" required>{r.get(key).decode("UTF-8")}</textarea>')
    except AttributeError:
        return "Invalid Message!"


@app.route('/reset', methods=["GET"])
def reset():
    if r.flushdb():
        return "Reset sucessfully."
    else:
        return "Reset failed."
