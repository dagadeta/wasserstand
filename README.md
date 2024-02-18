# Wasserstand
## Setup
1. Start the RPi and connect it to a network
2. Connect to the RPi over SSH and login
3. Install and configure [Apache](https://httpd.apache.org/)
4. Save index.html and check-water.py to the [file locations](#important-file-locations)
5. Execute `nohup python check-water.py`
6. Now you can open http://raspberrypi:8080/check-water to see the json output or http://raspberrypi/ to see the data visualised. If you want to see the data in your cli, you can execute `curl raspberrypi:8080/check-water`.
## Important file locations
* **index.html**: `/var/www/html`
* **check-water.py**: `/home/[user]`
