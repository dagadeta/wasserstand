import RPi.GPIO as GPIO
from http.server import BaseHTTPRequestHandler, HTTPServer

GPIO.setmode(GPIO.BCM)

hostName = ""
serverPort = 8080

# Define sensor pin numbers
sensor_pins = [5, 6, 13, 19, 26]

# Set up each sensor using a for loop
for i, sensor_pin in enumerate(sensor_pins, start=1):
    exec(f"sensor_{6 - i} = {sensor_pin}")
    GPIO.setup(sensor_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != "/check-water":
            self.send_response(404)
            self.end_headers()
            return

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(bytes("{", "utf-8"))
        self.wfile.write(bytes("\"sensor_5\": %s," % (self.is_low(sensor_5)), "utf-8"))
        self.wfile.write(bytes("\"sensor_4\": %s," % (self.is_low(sensor_4)), "utf-8"))
        self.wfile.write(bytes("\"sensor_3\": %s," % (self.is_low(sensor_3)), "utf-8"))
        self.wfile.write(bytes("\"sensor_2\": %s," % (self.is_low(sensor_2)), "utf-8"))
        self.wfile.write(bytes("\"sensor_1\": %s" % (self.is_low(sensor_1)), "utf-8"))
        self.wfile.write(bytes("}\n", "utf-8"))

    def is_low(self, sensor):
        is_low = GPIO.input(sensor) == GPIO.LOW
        return f"{is_low}".lower()


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    GPIO.cleanup()
    print("Server stopped.")
