# Wasserstand
## Setup
1. Start the RPi and connect it to a network
2. Connect to the RPi over SSH and login
3. Install and configure [Apache](https://httpd.apache.org/)
4. Save index.html and check-water.py to the [file locations](#important-file-locations)
5. Make the [Build](#build)
6. Execute `nohup python check-water.py`
7. Now you can open http://raspberrypi:8080/check-water to see the json output or http://raspberrypi/ to see the data visualised. If you want to see the data in your cli, you can execute `curl raspberrypi:8080/check-water`.

## Build
### What you need
* Raspberry Pi (I took a Raspberry Pi 4 Model B with 8Gb RAM)
* Resistor (Adapted to the required strength)
* Cable
### How it's built
* Position of the sensors at the water tank:
  * The 5 cables which serve as sensors are attached to the water tank at regular intervals. The bottom cable (sensor1) is about 5 cm above the bottom of the water tank and the top cable (sensor5) is about 5 cm below the top edge of the water tank.
  * GND is at the same height as sensor1. If this isn't enough at your water tank, you can also add more GND cables to the water tank.
* Sensor connections to the Raspberry Pi:
  * The GND cable is connected to the GND port of the Raspberry Pi. In between is a Resistor whose strength is adapted to the required strength.
  * The 5 cables which serve as sensors are attached to GPIO ports of the Raspberry Pi. In my case, they are:
    * sensor1: GPIO 26
    * sensor2: GPIO 19
    * sensor3: GPIO 13
    * sensor4: GPIO 6
    * sensor5: GPIO 5
  * If you want to use different GPIO ports, you have to change them in check-water.py.

## Important file locations
* **index.html**: `/var/www/html`
* **check-water.py**: `/home/[user]`
