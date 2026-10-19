FROM python:3.15

WORKDIR /app

RUN python3 -m venv /venv

RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=app/requirements.txt,target=requirements.txt \
    pip install --no-cache-dir -r requirements.txt

COPY ./app .

EXPOSE 8210

CMD ["python3", "./main.py"]