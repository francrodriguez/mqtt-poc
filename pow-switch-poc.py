#!/usr/bin/env python3


import paho.mqtt.client as mqtt

# This is the Publisher

client = mqtt.Client()
client.connect("192.168.1.218",1883,60)
client.publish("SONOFF-POWR2/relay/0/set", "1");
client.disconnect();
