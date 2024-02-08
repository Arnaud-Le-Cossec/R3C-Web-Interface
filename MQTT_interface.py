#******************************************************************************
# MQTT INTERFACE
# This program is part of the R3C Project
# Written by Arnaud LE COSSEC
# Revision 1.0 (08/02/2024)
#******************************************************************************

import paho.mqtt.client as mqtt
import simplejson as json
"""
broker_url = 'eu1.cloud.thethings.network'
broker_port = 1883

broker_client_id = "Data_Server"
broker_username = 'r3c-app@ttn'
broker_password = 'NNSXS.UKLO6VALTA655HZJISBOC42TCBUBSMIDWZ3EQJI.L6GO3BQ2H6LLYCX3BWUENUI3CPTAR42OFWUMTBOZO44WHZMYAO3A'
"""


#******************************************************************************
# MQTT CALLBACKS
#******************************************************************************

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print("Failed to connect, return code %d\n", rc)

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(broker_topic)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    #print(msg.topic+" "+str(msg.payload))
    #print(msg.payload)
    data = json.loads(msg.payload)
    battery = data['uplink_message']['decoded_payload']['bat']
    humidity = data['uplink_message']['decoded_payload']['hum']
    temperature = data['uplink_message']['decoded_payload']['temp']
    device_id = data['end_device_ids']['device_id']
    print("device ID = " + device_id + "; bat = " + str(battery) + "; temp = " + str(temperature) +"; humidity = "+ str(humidity))


#******************************************************************************
# MAIN
#******************************************************************************

#Load settings
try:
    file = open("/mqtt-interface/settings.json")
    settings = json.load(file)
    file.close()
except Exception as err:
    print("Error while loading settings.json")
    print(err)
    quit()

# Connect to the MQTT brocker
#client = mqtt.Client()
#client.on_connect = on_connect
#client.on_message = on_message
#client.username_pw_set(broker_username, broker_password)
#client.connect(broker_url, broker_port)

broker_topic = "v3/"+settings["broker_user"]+"/devices/+/up"

#Connect to MQTT broker
mqtt_client = mqtt.Client(clean_session=True)
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message
mqtt_client.username_pw_set(settings["broker_user"],settings["broker_password"])
mqtt_client.connect(settings["broker_url"], settings["broker_port"])

# Connect to the database


# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
mqtt_client.loop_forever()
