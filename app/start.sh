#!/bin/sh
python db_creation.py &&
python testes.py &&
python -u -i app.py
