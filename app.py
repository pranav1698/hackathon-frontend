import base64  # for encoding the script for variable

import os
import re
import json
from flask import Flask, flash, render_template, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename

# Initialize the Flask application
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form['email']
        TRAVIS_TAG = request.form['TRAVIS_TAG']
        event_url = request.form['event_url']
        with open('travis_script_1.sh', 'rb') as f:
            os.environ["TRAVIS_SCRIPT"] = str(base64.b64encode(f.read()))[1:]
        return redirect(url_for('output'))
    return render_template('index.html')


# Return a custom 404 error.
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


@app.errorhandler(500)
def application_error(e):
    # Return a custom 500 error.
    return 'Sorry, unexpected error: {}'.format(e), 500


if __name__ == '__main__':
    app.run()
