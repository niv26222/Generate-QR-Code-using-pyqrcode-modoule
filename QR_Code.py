# Python program to Generate QR Code using pyqrcode modoule.


import pyqrcode

from pyqrcode import QRCode

# String which represent the QR code
s = "I love Python"

# Generate QR code
url = pyqrcode.create(s)

# Create and save the svg file naming "myqr.svg"
url.svg("myqr.svg", scale = 8)

 