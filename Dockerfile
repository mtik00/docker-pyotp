FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN apt-get update \
&& apt-get install -y xclip tini \
&& pip install --no-cache-dir pyotp pyperclip

WORKDIR /usr/src/app
COPY ./src .
ENTRYPOINT [ "/usr/bin/tini", "--", "python3", "app.py" ]
