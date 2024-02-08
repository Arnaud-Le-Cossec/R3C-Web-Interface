FROM python:3.12

ADD MQTT_interface.py /mqtt-interface/

RUN pip install simplejson paho-mqtt psycopg2

USER root

CMD ["python3", "-u", "/mqtt-interface/MQTT_interface.py"] 
