develop :
    rm -rf .venv
    python -m venv .venv
    .venv/Scripts/activate
    pip install uv
    uv sync