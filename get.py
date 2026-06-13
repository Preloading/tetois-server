
from jinja2 import Environment, FileSystemLoader
from datetime import timedelta, datetime
import json

env = Environment(loader=FileSystemLoader('templates'))

def template(file, render_data):
    t = env.get_template(file)
    output = t.render(render_data)
    return output
