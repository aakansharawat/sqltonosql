# SQL to NoSQL Transpiler

This project parses a limited subset of SQL (ANTLR4), converts it into a unified AST (UAST),
and generates output for:

- MongoDB
- Cassandra (CQL)
- DynamoDB (boto3)
- Redis (command hints + limitations)

## What to run

### 1) Web UI (Flask)

From the project root:

```bash
cd /home/aakansha/sql-parser-project
source .venv/bin/activate
pip install -r web/requirements.txt
cd web
python server.py
```

Open: `http://localhost:5000`

### 2) CLI

From the project root:

```bash
python main.py "SELECT name, age FROM users WHERE age > 25 LIMIT 10" --target mongodb
python main.py "SELECT name FROM users WHERE age > 25" --target cassandra
python main.py "SELECT * FROM products LIMIT 5" --target dynamodb
python main.py "SELECT * FROM logs LIMIT 10" --target redis
```

### 3) End-to-end pipeline tests

```bash
python tests/test_pipeline.py
```

## Supported target ids

Use `--target` (CLI) or the dropdown (Web UI):
`mongodb`, `cassandra`, `dynamodb`, `redis`

