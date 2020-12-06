import base64
import ttn

class MqttClient:
    def __init__(self, access_key, app_id, device_id):
        self._ttn_handler = ttn.HandlerClient(app_id, access_key).data()
        self._ttn_handler.set_uplink_callback(self._uplink_callback)
        self._device_id = device_id
        self._uplink_observers = []

    def __enter__(self):
        self._ttn_handler.connect()
        return self

    def __exit__(self, *args):
        self._ttn_handler.close()

    def send(self, message):
        payload = base64.b64encode(message.encode()).decode()
        self._ttn_handler.send(self._device_id, payload)

    def register_uplink_observer(self, observer):
        self._uplink_observers.append(observer)

    def _uplink_callback(self, message, client):
        purified_payload = self._purify_payload(message.payload_fields.text)
        for uplink_observer in self._uplink_observers:
            uplink_observer.notify(purified_payload)

    def _purify_payload(self, payload):
        termination_index = payload.find('\0')
        if termination_index != -1:
            payload = payload[0:termination_index]

        return payload
