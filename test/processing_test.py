import unittest

from anima.processing import SentenceGenerator, SentenceMapping, Jinja2ParamsResolver


class SentenceGeneratorTest(unittest.TestCase):

    def test_inner_param(self):
        """Check the inner type resolving"""
        _mapping = SentenceMapping({
            "hello {{greeting}}": ["bonjour {{greeting}}"],
            "mister {{name}}": ["monsieur {{name}}"],
            "miss {{name}}": ["madame {{name}}"],
        })
        generator = SentenceGenerator(_mapping, Jinja2ParamsResolver())

        actual = generator.generate("hello {{greeting}}", [{
            "name": "greeting",
            "type": "inner",
            "value": "mister {{name}}"
        }, {
            "name": "name",
            "type": "string",
            "value": "Robert"
        }])

        self.assertEqual("bonjour monsieur Robert", actual)
