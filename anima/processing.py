from random import randint
from typing import Dict, List

import yaml
from jinja2 import Template


class SentenceMapping(object):
    def __init__(self, mapping: Dict[str, List[str]]):
        self._mapping = mapping

    def get_sentence(self, tag: str):
        result = self._mapping.get(Normalizer.normalize_sentence(tag), [tag])
        random_index = randint(0, len(result) - 1)
        return result[random_index]


class Jinja2ParamsResolver(object):
    def __init__(self):
        pass

    @staticmethod
    def resolve(sentence: str, params: Dict[str, object]):
        t = Template(sentence)
        return t.render(**params)


class SentenceGenerator(object):
    def __init__(self, sentence_mapping: SentenceMapping, params_resolver: Jinja2ParamsResolver):
        self._sentences_mapping = sentence_mapping
        self._params_resolver = params_resolver

    def generate(self, sentence: str, req_params: List[Dict[str, object]]):
        translated_sentence = self._sentences_mapping.get_sentence(sentence)
        params = {}
        for p in req_params:
            params[p["name"]] = self.process_value(p, req_params)

        return self._params_resolver.resolve(translated_sentence, params)

    @staticmethod
    def process_time(val) -> str:
        return val

    def process_enumerated_list(self, val) -> str:
        if len(val) == 1:
            return val[0]
        start = ", ".join(val[:-1])
        return "{0} {1} {2}".format(start, self._sentences_mapping.get_sentence("and"), val[-1])

    def process_value(self, param, req_params: List[Dict[str, object]]) -> str:
        if "type" not in param or param["type"] == "string":
            return param['value']

        if param["type"] == "time":
            return self.process_time(param['value'])

        if param["type"] == "enumerated_list":
            return self.process_enumerated_list(param['value'])

        if param["type"] == "inner":
            new_params = list(req_params)
            new_params.remove(param)
            return self.generate(param['value'], new_params)

        return param['value']


class Normalizer(object):
    @staticmethod
    def normalize_sentence(text):
        return text.lower()

    @staticmethod
    def normalize_dict_keys(d):
        return {Normalizer.normalize_sentence(key): value for key, value in d.items()}


class SentenceMappingReader(object):
    def __init__(self, file_path):
        self._file_path = file_path

    def build(self):
        with open(self._file_path, 'r') as stream:
            try:
                _mapping = yaml.load(stream)
                return SentenceMapping(Normalizer.normalize_dict_keys(_mapping))
            except yaml.YAMLError as e:
                print("Error ", e)
                return None
