import functools
import requests
import json

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash


bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/login', methods=('GET', 'POST'))
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
                # data = r.json()
                return r.text
            except requests.exceptions.Timeout:
                error = "timeout"
            except requests.exceptions.TooManyRedirects:
                error = "too many redirects"
            except requests.exceptions.RequestException as e:
                raise SystemExit(e)
            else:
                return data

    return error


@bp.route('/authdata', methods=('GET', 'POST'))
def datafetch():
    if request.method == 'GET':
        error = None
        try:
            r = requests.get(
                'https://6u3td6zfza.execute-api.us-east-2.amazonaws.com/prod/user/transactions')
            print(r.text)
            # data = r.json()
            return r.text
        except requests.exceptions.Timeout:
            error = "timeout"
        except requests.exceptions.TooManyRedirects:
            error = "too many redirects"
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
        else:
            return data
    return error
