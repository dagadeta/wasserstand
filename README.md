# Wasserstand
## Setup
1. Start the RPi and connect it to a network
2. Connect to the RPi over SSH and login as johannes
3. Execute `nohup python check-water.py`
4. Now you can open http://raspberrypi:8080/check-water to see the json output or http://raspberrypi/ to see the data visualised. If you want to see the data in your cli, you can execute `curl raspberrypi:8080/check-water`.
