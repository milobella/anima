# Anima
Anima manage the NLG (Natural Language Generation) part of milobella.

Main purposes :
- Generated sentences should be understandables;
- Should be also grammatically correct;
- All sentences of an anima entity should seems to come from a unique person, with a temper, an identity;
- Sentences should be adapted to the person who is speaking.

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

```bash
curl -i -X POST http://localhost:9333/restitute -d '{"sentence": "It is {{time}}", "params": [{"name": "time", "type": "time", "value": "15h"}]}'
```

## CHANGELOGS
- [Application changelog](./CHANGELOG.md)
- [Helm chart changelog](./helm/anima/CHANGELOG.md)