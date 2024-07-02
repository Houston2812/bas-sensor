FROM python:3.13.0a2-alpine3.17

WORKDIR /sensor

RUN mkdir -p /sensor/logs
COPY ./requirements.txt /sensor/requirements.txt
COPY ./src  /sensor/src
EXPOSE 5000
RUN pip3 install -r /sensor/requirements.txt
RUN sh -c 'echo SENSOR_DIR="$(pwd)" > src/.env'
CMD ["python3", "/sensor/src/sensor.py"]


