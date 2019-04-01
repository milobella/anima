# Installation
```bash
pip install -r requirements.txt
pip install -e .
```

# Run
```bash
anima_launcher
```

# Example of request

```bash
curl -i -X POST http://anima:9333/restitute -d '{"sentence": "It is {{time}}", "params": [{"name": "time", "type": "time", "value": "15h"}]}'
```