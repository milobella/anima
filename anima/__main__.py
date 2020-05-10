#!/usr/bin/env python
# coding: utf8

import configparser

from sanic import response, Sanic
from sanic.request import Request
from anima.processing import SentenceMappingReader, Jinja2ParamsResolver, SentenceGenerator

# Initialize the config
_config = configparser.ConfigParser()
_config.read('anima.ini')

# Initialize the sanic app
_app = Sanic(name="anima")

# Initialize the Natural Language Generator
_sentence_generator = SentenceGenerator(
    SentenceMappingReader(_config['sentences']['mapping_file']).build(),
    Jinja2ParamsResolver())


def main():
    # Run the vibora app
    _app.run(
        host=_config['server']['url'],
        port=_config['server'].getint('port')
    )


@_app.route('/')
async def home(_):
    return response.html('<p>Hello world!</p>')


@_app.route('/restitute', methods=["POST"])
async def restitute(request: Request):
    return response.text(_sentence_generator.generate(request.json["sentence"], request.json.get("params", [])))


if __name__ == '__main__':
    main()
