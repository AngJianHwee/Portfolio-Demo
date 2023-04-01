# -*- coding: utf-8 -*-
# @Author: Ang Jian Hwee
# @Date:   2022-09-19 22:58:23
# @Last Modified by:   Ang Jian Hwee
# @Last Modified time: 2022-12-11 03:31:22

from flask import Flask, render_template_string, request, redirect, render_template, url_for
import redis
import datetime
from werkzeug.utils import secure_filename
import hashlib

try:
    r = redis.Redis("redis-1bbf2d0d-nightorb-d1fc.aivencloud.com", 21416, 0,
                    'AVNS_RjXI0p9WSMhwkj2j1RW')
    r.ping()
except:
    r = redis.Redis("redis-10701.c62.us-east-1-4.ec2.cloud.redislabs.com",
                    10701, 0, 'G5geqLgrwhoY569qaXYWcX6oNCHdFWht')
    r.ping()

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "."


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
    r.incr("cur_increment")

    key = f'A{cur_increment:04d}'
    ttl = r.ttl(key)

    return render_template(
        "newMessage.html",
        content=r.get(key).decode("UTF-8"),
        ttl=ttl,
        exp_datetime=(
            datetime.datetime.now() +
            datetime.timedelta(seconds=ttl)).strftime("%m/%d/%Y %H:%M:%S"),
        url=f"/message/A{cur_increment:04d}",
        host_url=request.host_url[:-1])


@app.route('/message/<key>', methods=["GET"])
def message(key):
    try:
        ttl = r.ttl(key)
        return render_template(
            "text.html",
            content=r.get(key).decode("UTF-8"),
            ttl=ttl,
            exp_datetime=(
                datetime.datetime.utcnow() +
                datetime.timedelta(hours=8) +
                datetime.timedelta(seconds=ttl)).strftime("%m/%d/%Y %H:%M:%S"))
    except AttributeError:
        return render_template('invalidMessage.html')


@app.route('/reset', methods=["GET"])
def _reset():
    if r.flushdb():
        reset_status = "Success"
    else:
        reset_status = "Failed"
    return render_template('reset.html', reset_status=reset_status)


@app.route('/status', methods=["GET"])
def _status():
    return render_template_string(
        str(
            vars(vars(r)['connection_pool'])['connection_kwargs']
            ['host'].split(".")[-2]))


@app.route('/latest', methods=["GET"])
@app.route('/l', methods=["GET"])
def latest():
    cur_increment = int(r.get("cur_increment").decode('UTF-8')) - 1
    key = f'A{cur_increment:04d}'

    # return redirect(url_for('message', key=key), code=302)

    try:
        ttl = r.ttl(key)

        return render_template(
            "text.html",
            content=r.get(key).decode("UTF-8"),
            ttl=ttl,
            exp_datetime=(
                datetime.datetime.utcnow() +
                datetime.timedelta(hours=8) +
                datetime.timedelta(seconds=ttl)).strftime("%m/%d/%Y %H:%M:%S"),
            url=f"/message/{key}",
            host_url=request.host_url[:-1])
    except AttributeError:
        return render_template('invalidMessage.html')

    #
