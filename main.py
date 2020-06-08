# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 16:13:14 2020

@author: Humberto
"""

import os

import time
import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_time():
 
    return str(round(time.time()))
    

@app.route('/')
def home():
    curr_time = get_time()
    return curr_time


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)