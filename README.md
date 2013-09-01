# mqtt-dbus

Subscribe to a topic and desktop notifications are sent if a message about a 
specific MQTT topic arrives.

## Prerequisites/Installation

### Get the files
Clone the `mqtt-dbus` [repository](https://github.com/fabaff/mqtt-dbus):
```
git clone git@github.com:fabaff/mqtt-dbus.git
```

###Dependencies
`mqtt-dbus` depends on a couple of additional pieces: 

- [mosquitto](http://mosquitto.org/)
- [dbus-python](http://www.freedesktop.org/wiki/Software/DBusBindings/)

```
sudo yum -y install dbus-python mosquitto
```

## Usage
Make the _mqtt-dbus.py_ file executable and run it.

```
./mqtt-dbus.py
```

## License
`mqtt-dbus` licensed under MIT, for more details check LICENSE.
