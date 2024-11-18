#!/bin/bash

source .venv/*/bin/activate
uvicorn --ssl-keyfile=potestades.com.key --ssl-certfile=potestades.com.cert main:app --host 0.0.0.0
