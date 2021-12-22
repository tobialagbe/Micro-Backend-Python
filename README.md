# Python-Backend

This project was built with Flask 2.0 and python 3.10.

## Getting Started

run `docker build --tag python-docker .` then `docker run -d -p 5000:5000 python-docker`

## routes

This application receives requests on three routes `auth/login`,`auth/authdata` and `auth/cancel`. Login and cancel are Post requests while authdata is a get request.
