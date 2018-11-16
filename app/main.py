# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START app]
import logging

# [START imports]
from flask import Flask, render_template, redirect, url_for, request, session, flash
import json
# [END imports]

from functools import wraps

# [START create_app]
app = Flask(__name__)
# [END create_app]


# [START form]
app.secret_key = "for your eyes only"

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            print("Check 2")
            return f(*args, **kwargs)
        else:
            render_template('sign_in.html')
    return wrap


@app.route('/log_in', methods=['GET', 'POST'])
def sign_in():
    if request.method == 'POST':
        with open('static/users/users.json', encoding='utf-8-sig') as json_file:
            text = json_file.read()
            json_data = json.loads(text)

        for row in json_data:
            if (request.form["username"] == row["username"]) and request.form["password"] == row["password"]:
                session['logged_in'] = True
                session['username'] = request.form["username"]
                return redirect(url_for('data1'))

    return render_template('sign_in.html')

@app.route('/data-1')
#@login_required
def data1():
    return render_template('data_studio.html')
    
@app.route('/data-2')
@login_required
def data2():
    return render_template('data_studio2.html')
    
    
@app.route('/data-3')
@login_required
def data3():
    return render_template('data_studio3.html')

@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        with open('static/users/users.json', encoding='utf-8-sig') as json_file:
            text = json_file.read()
            json_data = json.loads(text)

        for row in json_data:
            if (request.form["username"] == row["username"]) and request.form["password"] == row["password"]:
                session['logged_in'] = True
                session['username'] = request.form["username"]
                return redirect(url_for('data1'))

    return render_template('home.html')

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout_page():
        session.pop('logged_in', None)
        session.pop('user', None)
        return redirect(url_for('home'))

@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
    app.run(debug=True)
