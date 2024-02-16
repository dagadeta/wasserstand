import RPi.GPIO as GPIO
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

GPIO.setmode(GPIO.BCM)

hostName = ""
serverPort = 8080

sensor_5 = 5
GPIO.setup(sensor_5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
sensor_4 = 6
GPIO.setup(sensor_4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
sensor_3 = 13
GPIO.setup(sensor_3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
sensor_2 = 19
GPIO.setup(sensor_2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
sensor_1 = 26
GPIO.setup(sensor_1, GPIO.IN, pull_up_down=GPIO.PUD_UP)


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != "/check-water":
            self.send_response(404)
            self.end_headers()
            return

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(bytes("{", "utf-8"))
        self.wfile.write(bytes("\"sensor_5\": %r," % (GPIO.input(sensor_5) == GPIO.LOW), "utf-8"))
        self.wfile.write(bytes("\"sensor_4\": %r," % (GPIO.input(sensor_4) == GPIO.LOW), "utf-8"))
        self.wfile.write(bytes("\"sensor_3\": %r," % (GPIO.input(sensor_3) == GPIO.LOW), "utf-8"))
        self.wfile.write(bytes("\"sensor_2\": %r," % (GPIO.input(sensor_2) == GPIO.LOW), "utf-8"))
        self.wfile.write(bytes("\"sensor_1\": %r" % (GPIO.input(sensor_1) == GPIO.LOW), "utf-8"))
        self.wfile.write(bytes("}\n", "utf-8"))


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
