#!/usr/bin/python3
""" set the status route with app_views blueprint """
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status')
def show_status():
    """ returns the status of the link /status """
    result = {"status": "OK"}
    return (jsonify(result))
