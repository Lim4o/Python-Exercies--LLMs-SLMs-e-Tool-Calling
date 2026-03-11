# Python Exercises: LLMs, SLMs, and Tool Calling

This repository contains hands-on Python exercises that demonstrate tool
calling (function calling) with Groq models. Each exercise focuses on a
specific use case, from simple arithmetic to weather and scheduling.

## Learning Goals

- Expose Python functions as callable tools
- Let the model choose the correct function from natural language input
- Parse tool arguments returned by the model
- Keep orchestration logic separate from domain logic (`tools.py`)

## Project Structure

| Exercise | Scenario                                          | Entry Script                    |
| -------- | ------------------------------------------------- | ------------------------------- |
| Ex1      | Basic calculator (sum and multiply)               | `Ex1/calculadoraSimples.py`     |
| Ex2      | Full calculator (add, subtract, multiply, divide) | `Ex2/calculadoraCompleta.py`    |
| Ex3      | Temperature conversion                            | `Ex3/conversaoDeTemperatura.py` |
| Ex4      | Product price lookup                              | `Ex4/consultaDeProduto.py`      |
| Ex5      | Stock verification                                | `Ex5/veridicacaoDeEstoque.py`   |
| Ex6      | Agenda system                                     | `Ex6/sistemaDeAgenda.py`        |
| Ex7      | Weather lookup                                    | `Ex7/consultaDeClima.py`        |

Each exercise folder includes:

- an entry script with Groq tool-calling orchestration
- a `tools.py` file containing the executable domain functions

## Tech Stack

- Python 3
- [groq](https://pypi.org/project/groq/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

## Prerequisites

- Python 3.11 or newer
- A valid Groq API key

## Setup

From the repository root:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install groq python-dotenv
```

Create your environment file and set your API key:

```powershell
Copy-Item .env.example .env
```

Then edit `.env` and set:

```env
GROQ_API_KEY=your_real_groq_api_key
```

## Run the Exercises

From the repository root:

```powershell
.\.venv\Scripts\python.exe Ex1\calculadoraSimples.py
.\.venv\Scripts\python.exe Ex2\calculadoraCompleta.py
.\.venv\Scripts\python.exe Ex3\conversaoDeTemperatura.py
.\.venv\Scripts\python.exe Ex4\consultaDeProduto.py
.\.venv\Scripts\python.exe Ex5\veridicacaoDeEstoque.py
.\.venv\Scripts\python.exe Ex6\sistemaDeAgenda.py
.\.venv\Scripts\python.exe Ex7\consultaDeClima.py
```

If you are inside `Ex7`, run:

```powershell
..\.venv\Scripts\python.exe .\consultaDeClima.py
```

## Common Pitfall

This command is invalid:

```powershell
pip python .\consultaDeClima.py
```

Use `python` to execute scripts, and `pip` only to install packages.
