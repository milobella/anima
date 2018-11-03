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


@_app.route('/restitute', methods=["POST"])
async def restitute(request: Request):
    translated_sentence = _mapping.get_sentence(request.json["sentence"])
    params = request.json.get("params", {})
    return response.text(Jinja2Resolver.resolve(translated_sentence, params))


if __name__ == '__main__':
    main()
