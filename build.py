#!/usr/bin/env python
import json
import os
import requests

def send_trigger_request(query, languagecode):
    USER = 'pranav1698'
    PROJECT = 'backend'
    BRANCH = 'master'
    KEY = 'kvlbiNNwP5rCUQmQ_gmMxA'
    travis_api_url = 'https://api.travis-ci.org/repo/{}%2F{}/requests'.format(USER, PROJECT)
    request_body = {}
    request = {}
    request['branch'] = BRANCH
    request['config'] = {}
    request['config']['env'] = {}
    request['config']['env']['query'] = query
    request['config']['env']['languagecode'] = languagecode
    request_body['request'] = request
    request_body = json.dumps(request_body)
    headers = { "Content-Type": "application/json", "Accept": "application/json", "Travis-API-Version": "3", "Authorization": "token {}".format(KEY)}

    response = requests.post(travis_api_url, headers=headers, data=request_body)

    if response.status_code == 202:
        print('Trigger successful')
    else:
        print('Trigger failed, response code {}'.format(response.status_code))


