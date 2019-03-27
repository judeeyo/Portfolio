''''**************************************************
 * Copyright (c) 2019 JOO-YOUNG LEE. To Present
 * All rights reserved.
 **************************************************'''
#!/usr/bin/python
#-*- coding: utf-8 -*-
import re
import os
import sys
import time
import urllib
import logging
import argparse
import datetime
import subprocess
import threading
import subprocess
import logging.handlers
import stat
import json
from flask import *
from jinja2 import *
from collections import OrderedDict
import csv
try:
    import simplejson as json
except:
    import json


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser(description="")
        parser.add_argument('--listen-port', type=str, required=True, help='REST service listen port')
        args = parser.parse_args()
        listen_port = args.listen_port

    except Exception as e:
        print('Error: %s' % str(e))
    # TODO bctak: Need to select one IP that is externally visible. Currently, it just picks the first one.
    ipaddr = subprocess.getoutput("hostname -I").split()[0]
    print('Starting the service with ip_addr=' + ipaddr)
    app.run(debug=False, host=ipaddr, port=int(listen_port))