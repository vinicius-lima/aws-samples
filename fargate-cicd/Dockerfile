FROM python:3.6-slim

EXPOSE 80

ENV API_KEY empty

WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir \
    Flask \
    Flask-Cors

COPY ./service.py /usr/src/app

CMD [ "python", "-u", "./service.py" ]
