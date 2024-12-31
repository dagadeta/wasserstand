# Wasserstand
## Content
- [Setup](#setup)
  - [Hardware](#hardware)
    - [What you need](#what-you-need)
    - [How it's built](#how-its-built)
- [Important File Locations](#important-file-locations)
- [Server Endpoint (`/check-water`)](#server-endpoint-check-water)
  - [Response Overview](#response-overview)
  - [Structure of the Response](#structure-of-the-response)
    - [Example JSON Response](#example-json-response)


## Setup
1. Start the RPi and connect it to a network
2. Connect to the RPi over SSH and login
3. Install and configure [Apache](https://httpd.apache.org/)
4. Save index.html and check-water.py to the [file locations](#important-file-locations)
5. Set up the [Hardware](#hardware)
6. Execute `nohup python check-water.py`
7. Now you can open http://raspberrypi:8080/check-water to see the JSON output or http://raspberrypi/ to see the data visualized. If you want to see the data in your cli, you can execute `curl raspberrypi:8080/check-water`.

### Hardware
#### What you need
- Raspberry Pi (I took a Raspberry Pi 4 Model B with 8Gb RAM)
- Resistor (Adapted to the required strength)
- Cable
#### How it's built
- Position of the sensors at the water tank:
  - The five cables which serve as sensors are attached to the water tank at regular intervals. The bottom cable (sensor1) is about 5 cm above the bottom of the water tank, and the top cable (sensor5) is about 5 cm below the top edge of the water tank.
  - GND is at the same height as sensor1. If this isn't enough at your water tank, you can also add more GND cables to the water tank.
- Sensor connections to the Raspberry Pi:
  - The GND cable is connected to the GND port of the Raspberry Pi. In between is a Resistor whose strength is adapted to the required strength.
  - The five cables which serve as sensors are attached to GPIO ports of the Raspberry Pi. In my case, they are:
    - sensor1: GPIO 26
    - sensor2: GPIO 19
    - sensor3: GPIO 13
    - sensor4: GPIO 6
    - sensor5: GPIO 5
  - If you want to use different GPIO ports, you have to change them in check-water.py.


## Important file locations
- **index.html**: `/var/www/html`
- **check-water.py**: `/home/[user]`

## Server endpoint (`/check-water`)
The Raspberry Pi server receives HTTP GET requests
and sends back a response containing water level sensor statuses in JSON format.
This section describes the structure of the response and guides users on how to access it.
This might be useful for you if you want to run the water level check on the Raspberry Pi with your own usage of it.

### Response overview
The server is a simple HTTP server running on the Raspberry Pi.
When a GET request is sent to the `/check-water` endpoint,
the server responds with the current statuses of five water level sensors.
Each sensor status is represented as a boolean value.

It's worth noting here that even though the server runs in python, it responds with lowercase booleans.
This is because most languages use lowercase booleans, and so I changed them to make the processing of the data easier.

### Structure of the response
After a successful GET request to `/check-water`, the server responds with:
- **HTTP Status Code**: `200 OK` (if the request is valid). If the requested endpoint is unavailable, the server responds with a `404 Not Found` status.
- **Content-Type**: `application/json`
- **Access-Control-Allow-Origin**: `*` (to allow CORS)

The body of the response is a JSON object containing five key-value pairs,
where each key represents a sensor (e.g., `sensor_1`, `sensor_2`, etc.),
and the value represents the status of the sensor
(`true` or `false`).
#### Example JSON Response:
``` json
{
  "sensor_5": false,
  "sensor_4": false,
  "sensor_3": true,
  "sensor_2": true,
  "sensor_1": true
}
```

**Explanation of the Response:**
- `sensor_5`: Refers to the sensor closest to the top of the tank.
- `sensor_1`: Refers to the sensor closest to the bottom of the tank.


- `true`: The sensor detects water at its position.
- `false`: The sensor does not detect water at its position.

With that information, we can see that our example water tank is 3/5 full of water.