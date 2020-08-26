#!/usr/bin/python

import json
import time
from flask import Flask, redirect, send_from_directory
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)


@app.route('/')  # เมื่อเข้ามาที่ root
def index():
    return redirect("/web/index.html", code=302)


@app.route("/web")  # เผื่อมีใครพิมพ์ /web เข้ามาตรงๆ
def home_page():
    return redirect("/web/index.html", code=302)


@app.route('/web/<path:filename>')  # ใช้ static html จาก folder static
def static_files(filename):
    return send_from_directory("./static", filename)


# Start flask
if __name__ == '__main__':
    app.run(threaded=True)
