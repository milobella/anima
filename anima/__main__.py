#!/usr/bin/env python
# coding: utf8

import configparser

from sanic import response, Sanic
from sanic.request import Request
from sanic.response import json

# Initialize the config
from anima.processing import SentenceMappingReader, Jinja2Resolver

_config = configparser.ConfigParser()
_config.read('anima.ini')

# Initialize the sanic app
_app = Sanic()

_mapping = SentenceMappingReader(_config['sentences']['mapping_file']).build()


def main():
    # Run the vibora app
    _app.run(
        host=_config['server']['url'],
        port=_config['server'].getint('port')
    )


@_app.route('/')
async def home(request):
    return response.html('<p>Hello world!</p>')


def process_time(val):
    return val


def process_enumerated_list(val):
    if len(val) == 1:
        return val
    start = ", ".join(val[:-1])
    return "{0} {1} {2}".format(start, _mapping.get_sentence("and"), val[-1])


def process_value(param):
    if "type" not in param or param["type"] == "string":
        return param['value']
    elif param["type"] == "time":
        return process_time(param['value'])
    elif param["type"] == "enumerated_list":
        return process_enumerated_list(param['value'])


@_app.route('/restitute', methods=["POST"])
async def restitute(request: Request):
    translated_sentence = _mapping.get_sentence(request.json["sentence"])
    params = request.json.get("params", [])
    jinja_params = {}
    for p in params:
        jinja_params[p["name"]] = process_value(p)

    return response.text(Jinja2Resolver.resolve(translated_sentence, jinja_params))


if __name__ == '__main__':
    main()
