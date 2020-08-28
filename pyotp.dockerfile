FROM python:3.8-alpine


RUN apk update                      \
&& pip install --no-cache-dir pyotp

WORKDIR /usr/src/app
COPY ./main.py .
ENTRYPOINT [ "python3", "-B", "main.py" ]