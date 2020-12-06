import datetime

from influxdb import InfluxDBClient

class InfluxWriter:
    def __init__(self, configuration, location):
        self._db_client = InfluxDBClient(**configuration)
        self._location = location

    def notify(self, message):
        fields = self._extract_fields(message)
        entry = self._build_db_entry(fields)
        self._db_client.write_points(entry)

    def _extract_fields(self, message):
        fields = {}

        measurements = message.split(',')
        for measurement in measurements:
            colon_index = measurement.find(':')
            if measurement[0] == 'L':
                fields['light'] = float(measurement[colon_index + 1:])
            if measurement[0] == 'T':
                fields['temperature'] = float(measurement[colon_index + 1:])

        return fields

    def _build_db_entry(self, fields):
        return [
            {
                'measurement': 'light_and_temperature',
                'tags': {'location': self._location},
                'time': datetime.datetime.utcnow().isoformat(),
                'fields': fields
            }
        ]
