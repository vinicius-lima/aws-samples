FROM python:3.6-alpine

ENV SRV_NAME service_A
ENV SRV_HOST 0.0.0.0
ENV SRV_PORT 5080
ENV REMOTE_HOST localhost
ENV REMOTE_PORT 5080

WORKDIR /usr/src/app

RUN pip install --no-cache-dir \
    requests \
    Flask

COPY app/service.py .

EXPOSE 5080

CMD [ "python", "./service.py" ]
