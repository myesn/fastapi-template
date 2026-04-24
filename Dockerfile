FROM docker.1ms.run/astral/uv:python3.14-alpine

WORKDIR /project

COPY pyproject.toml uv.lock ./
COPY app/ ./app
COPY gunicorn.conf.py ./

RUN uv sync --frozen --no-dev

EXPOSE 8000

CMD ["uv", "run", "gunicorn", "app.main:app"]