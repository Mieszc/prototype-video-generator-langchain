# Setup Guide

This project uses a lean Python environment for LangChain and LangGraph.

## 1. Create a virtual environment

Using Python 3.12 is recommended.

```bash
python3.12 -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
py -3.12 -m venv .venv
.venv\Scripts\Activate.ps1
```

## 2. Upgrade packaging tools

```bash
python -m pip install --upgrade pip setuptools wheel
```

## 3. Install dependencies

From the project root:

```bash
pip install -r requirements.txt
```

Or, if you use uv:

```bash
uv sync
```

## 4. Optional: verify the environment

```bash
activate

```

## 5. Environment variables

If the project uses API keys or other secrets, create a local `.env` file in the project root and add the required values.

Example:

```env
OPENAI_API_KEY=your_key_here
```

## 6. Run the project

After installation, run your scripts from the project root with the virtual environment activated.
