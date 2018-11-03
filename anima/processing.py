from typing import Dict
from jinja2 import Template

import yaml


class SentenceMapping(object):
    def __init__(self, mapping: Dict[str, str]):
        self._mapping = mapping

    def get_sentence(self, tag: str):
        return self._mapping.get(Normalizer.normalize_sentence(tag), [tag])[0]


class Jinja2Resolver(object):
    def __init__(self):
        pass

    @staticmethod
    def resolve(sentence: str, params: Dict[str, object]):
        t = Template(sentence)
        return t.render(**params)


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
