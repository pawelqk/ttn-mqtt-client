from configuration import access_key, app_id, device_id, influx_conf
from influx_writer import InfluxWriter
from mqtt_client import MqttClient


def handle_input(mqtt_client):
    try:
        usr_input = input('Please provide input to send:\n')
        mqtt_client.send(usr_input)
    except EOFError:
        print('Terminating')
        return False

    return True


if __name__ == '__main__':
    print('MQTT client for TTN. Press CTRL+D to terminate')
    with MqttClient(access_key, app_id, device_id) as mqtt_client:
        mqtt_client.register_uplink_observer(InfluxWriter(influx_conf, 'Wroclaw'))
        while handle_input(mqtt_client):
            pass
