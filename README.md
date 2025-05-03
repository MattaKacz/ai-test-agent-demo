![Tests](https://github.com/MattaKacz/ai-test-agent/actions/workflows/run-tests.yml/badge.svg)

# AI Test Agent

An AI-powered tool that analyzes Python/Django source code and generates unit tests using GPT.

## 🚀 Features

- Parses Python source code (e.g., Django views)
- Sends code to a local LLM (LLaMA 3) via Ollama to generate pytest-based tests
- Saves generated tests in a `tests/` directory
- Automatically runs the tests and shows results

## 🧱 Project Structure

```
ai-test-agent/
├── agent/
│   ├── analyzer.py      # Extracts functions from source
│   ├── generator.py     # Sends code to GPT to generate tests
│   ├── runner.py        # Executes pytest
├── example/
│   └── views.py         # Example Django view
├── tests/               # Folder where tests are saved
├── .env                 # Your OpenAI API key
├── main.py              # Entry point
├── requirements.txt
```

## 🔒 Pre-commit Hooks

To enforce code formatting and linting locally before every commit, use [pre-commit](https://pre-commit.com):

```bash
pip install pre-commit
pre-commit install
```

This will automatically run `black` and `flake8` before each commit.

## ✅ Getting Started

1. **Install dependencies:**

```bash
pip install -r requirements.txt
```

2. **Make sure you have Ollama installed and a model (like llama3) pulled:**

```
ollama pull llama3
```

3. **Run the agent:**

```bash
python main.py
```

4. **See generated tests and results!**

## 🧠 Coming soon

- Class-based view (CBV) support
- Streamlit UI
- CI/CD integration

Enjoy!

## 📊 Test Coverage

This project uses `coverage.py` to generate test coverage reports.

To run it locally:

```bash
coverage run -m pytest tests/
coverage report
```

You can also generate an XML report for CI tools:

```bash
coverage xml
```
