FROM python:3.6-alpine

ENV SRV_HOST 0.0.0.0
ENV SRV_PORT 80

WORKDIR /usr/src/app

RUN pip install --no-cache-dir \
    Flask

COPY service.py .

EXPOSE 80

CMD [ "python", "./service.py" ]
