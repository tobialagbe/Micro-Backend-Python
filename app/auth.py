import functools
import requests
import json

from flask import (
    Blueprint, redirect, request
)
from flask_cors import CORS, cross_origin

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/login', methods=('GET', 'POST'))
@cross_origin()
def login():
    if request.method == 'POST':
        req_data = request.get_json()
        username = req_data['username']
        password = req_data['password']
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            try:
                data = {'Username': username, 'Password': password}
                r = requests.post(
                    'https://6u3td6zfza.execute-api.us-east-2.amazonaws.com/prod/user/login', data=json.dumps(data))
                print(r.text)
                return {
                    "error": False,
                    "data": r.text
                }
            except requests.exceptions.Timeout:
                error = "timeout"
            except requests.exceptions.TooManyRedirects:
                error = "too many redirects"
            except requests.exceptions.RequestException as e:
                raise SystemExit(e)

    return {
        "error": True,
        "data": error
    }


@bp.route('/authdata', methods=('GET', 'POST'))
@cross_origin()
def datafetch():
    if request.method == 'GET':
        error = None
        try:
            r = requests.get(
                'https://6u3td6zfza.execute-api.us-east-2.amazonaws.com/prod/user/transactions')
            print(r.text)
            return {
                "error": False,
                "data": r.text
            }
        except requests.exceptions.Timeout:
            error = "timeout"
        except requests.exceptions.TooManyRedirects:
            error = "too many redirects"
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

    return {
        "error": True,
        "data": error
    }


@bp.route('/cancel', methods=('GET', 'POST'))
@cross_origin()
def cancel():
    if request.method == 'POST':
        error = None
        req_data = request.get_json()
        try:
            with open("transaction.txt", "a") as fo:
                fo.write(json.dumps(req_data))
                fo.write("\n")
                fo.close()
            return {
                "error": False,
                "data": {
                    "code": 200,
                    "status": "Success"
                }
            }
        except:
            error = "Error cancelling transaction"
            return {
                "error": True,
                "data": error
            }
    return {
        "error": True,
        "data": "wrong http method"
    }
