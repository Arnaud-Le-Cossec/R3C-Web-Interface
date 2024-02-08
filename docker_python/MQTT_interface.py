import paho.mqtt.client as mqtt
import json

broker = 'eu1.cloud.thethings.network'
port = 1883

client_id = "Data_Server"
username = 'r3c-app@ttn'
password = 'NNSXS.UKLO6VALTA655HZJISBOC42TCBUBSMIDWZ3EQJI.L6GO3BQ2H6LLYCX3BWUENUI3CPTAR42OFWUMTBOZO44WHZMYAO3A'

topic = "v3/"+username+"/devices/+/up"


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print("Failed to connect, return code %d\n", rc)
    #print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(topic)

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

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(username, password)
client.connect(broker, port)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
