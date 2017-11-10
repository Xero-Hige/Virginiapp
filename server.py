import os
import random
import re
from subprocess import PIPE, Popen

from flask import Flask, redirect, render_template, request

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/', methods=["GET"])
def root():
    return render_template("template.html")

@app.route('/', methods=["POST"])
def add():
    return "Hola {}".format(request.json["name"])