#!/bin/python3

import sys
print("Content-type: image/png", end="\r\n\r\n", flush=True)
sys.stdout.buffer.write(bytes(open("/var/www/html/pic.jpg","rb").read()))

