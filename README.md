# Anima
Anima manages the NLG (Natural Language Generation) part of Milobella.

All sentences of an Anima entity should :
- be understandable,
- be grammatically correct,
- be available in several languages,
- seem to come from a unique person, with a temper, an identity,
- be adapted to the person who is speaking.

## Installation
```bash
pip install -r requirements.txt
pip install -e .
```

## Run
```bash
anima_launcher
```

## Example of request

### Sentence restitution
```bash
$ curl -X POST http://localhost:9333/api/v1/restitute -d '{"sentence": "It is {{time}}", "params": [{"name": "time", "type": "time", "value": "15h"}]}'
Il est 15h.
```

### Raw sentences
```bash
$ curl http://localhost:9333/api/v1/sentences
{"it is {{time}}":["Il est {{time}}"]}
```
