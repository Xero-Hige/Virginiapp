import os
import random
import re
from db_handler import DB_Handler
from subprocess import PIPE, Popen

from flask import Flask, redirect, render_template, request

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/', methods=["GET"])
def root():
    return render_template("template.html")

@app.route('/', methods=["POST"])
def add():
    with DB_Handler() as handler:
        handler.add(request.form["name"])

    return render_template("template.html")
