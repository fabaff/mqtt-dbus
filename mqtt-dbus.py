#!/usr/bin/env python
#
# Copyright (c) 2013 Fabian Affolter <fabian at affolter-engineering.ch>
#
# Released under the MIT license.
#
import dbus
import sys
import mosquitto

name='MQTT notifications'
broker = '127.0.0.1'
port = 1883
topic = 'test/#'
qos = 0

# Assign a callback for connect and disconnect
def on_connect(mosq, obj, rc):
    if rc == 0:
        print 'Connected successfully to %s:%s' % (broker, port)

def on_disconnect(mosq, obj, rc):
    print 'Not able to connect to %s:%s' % (broker, port)

# Send a notification after a new message has arrived
def on_message(mosq, obj, msg):
    message = msg.payload + ' \n(Topic: ' + msg.topic + ' - QoS: ' + str(msg.qos) + ')'
    notify(summary=msg.payload, body=message)

# Details: https://developer.gnome.org/notification-spec/
# http://cheesehead-techblog.blogspot.ch/2009/02/five-ways-to-make-notification-pop-up.html
def notify(summary, body):
    app_name = name
    replaces_id=0
    service = 'org.freedesktop.Notifications'
    path = '/org/freedesktop/Notifications'
    interface = service
    app_icon = '/usr/share/icons/gnome/32x32/places/network-server.png'
    expire_timeout = 1000
    actions = []
    hints = []

    session_bus = dbus.SessionBus()
    obj = session_bus.get_object(service, path)
    interface = dbus.Interface(obj, interface)
    interface.Notify(app_name, replaces_id, app_icon, summary, body, actions,
        hints, expire_timeout)

def main():
    # Setup the MQTT client
    mqttclient = mosquitto.Mosquitto('notify')
    mqttclient.connect(broker, port, 60)

    # Callbacks
    mqttclient.on_message = on_message
    mqttclient.on_connect = on_connect
    mqttclient.on_disconnect = on_disconnect

    # Subscribe to topic 'test'
    mqttclient.subscribe(topic, qos)

    # Loop the client forever
    while mqttclient.loop() == 0:
        pass

if __name__ == '__main__':
    main()
