"""A common measure of transmission for digital data is the baud rate, defined as
the number of bits transmitted per second. Generally, transmission is accom-
plished in packets consisting of a start bit, a byte (8 bits) of information, and a stop
bit. Using these facts, answer the following:

(a) How many minutes would it take to transmit a 1024*1024 image with 256
gray levels using a 56K baud modem?

(b) What would the time be at 750K baud, a representative speed of a phone
DSL (digital subscriber line) connection?"""

import numpy as np

bits_per_px = 8
num_px = (1024 * 1024)
start_stop_bits = num_px * 2

total_bits = (bits_per_px * num_px) + start_stop_bits

baud_rate_a = 56000

seconds = total_bits / baud_rate_a

print(f"Transmission of a 1024x1024 px image with 256 gray levels would take {round(seconds, 2)} seconds using a 56K baud modem,")

minutes = int(seconds//60)
remaining_seconds = int(seconds % 60)

print(f"approximately {minutes} minutes and {remaining_seconds} seconds.")

baud_b = 750000
seconds_b = total_bits / baud_b

print(f"Using a 750K baud reduces this time to {round(seconds_b, 2)} seconds.")