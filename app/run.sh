#!/bin/bash

cd app
gunicorn __init__:app 