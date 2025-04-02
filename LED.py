# Author: Renjie Zhou
# Date: 2025-04-02
# Description: A simple script to control an LED using Raspberry Pi's GPIO.

# Import RPi.GPIO library as GPIO - this allows control of Raspberry Pi GPIO pins
import RPi.GPIO as GPIO

# Import time library for adding delays/pauses
import time

# Set GPIO pin numbering mode to BCM
# BCM mode uses Broadcom chip's GPIO numbering rather than physical pin numbers
GPIO.setmode(GPIO.BCM)

# Disable GPIO warnings
# This avoids warning messages if pins have been previously set to other uses
GPIO.setwarnings(False)

# Set GPIO pin 18 as output
# This means we can control this pin to output HIGH or LOW voltage
GPIO.setup(18, GPIO.OUT)

# Print "LED on" message to terminal indicating LED will turn on
print("LED on")

# Set GPIO 18 to HIGH (3.3V)
# This allows current to flow through the circuit, lighting the LED
GPIO.output(18, GPIO.HIGH)

# Pause the program for 1 second
# During this time the LED remains lit
time.sleep(1)

# Print "LED off" message to terminal indicating LED will turn off
print("LED off")

# Set GPIO 18 to LOW (0V)
# This cuts off current, turning off the LED
GPIO.output(18, GPIO.LOW)
