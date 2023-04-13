"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgrq40ndvk4rjsv9i8t0-a.oregon-postgres.render.com",
        database="todo_7anx",
        user="root1",
        password="a4tpg3SSSmCflqc9X4fHeLMembDshgMK")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
