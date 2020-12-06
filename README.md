# ttn-mqtt-client

App that sends data from stdin to your node device via LoRaWAN gateway and gathers the data sent from the node device to the InfluxDB.


## Installation
```bash
python -m venv venv
source venv/bin/activate  # or equivalent for your shell
pip install --upgrade pip
pip install -r requirements.txt
```

## Configuration
Provide all the configuration for LoRaWAN and InfluxDB in configuration.py file.

## Running
```bash
python main.py
```
