# Author: Renjie Zhou
# Date: 2025-04-02
# Python knowledge quiz with LED feedback (correct=green, incorrect=red)

import RPi.GPIO as GPIO  # Import GPIO library for Raspberry Pi control
import time              # Import time library for delays

# GPIO Setup
GPIO.setmode(GPIO.BCM)           # Use Broadcom (BCM) pin numbering
GPIO.setwarnings(False)          # Disable GPIO warnings
GREEN_LED = 17                   # Green LED connected to GPIO17
RED_LED = 18                     # Red LED connected to GPIO18

# Set GPIO pins as outputs
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)

def control_led(is_correct):
    """Control LEDs based on answer correctness
    Args:
        is_correct (bool): True for correct answer, False for incorrect
    """
    if is_correct:
        GPIO.output(GREEN_LED, GPIO.HIGH)  # Turn on green LED
        time.sleep(1)                      # Keep on for 1 second
        GPIO.output(GREEN_LED, GPIO.LOW)   # Turn off green LED
    else:
        GPIO.output(RED_LED, GPIO.HIGH)    # Turn on red LED
        time.sleep(1)
        GPIO.output(RED_LED, GPIO.LOW)     # Turn off red LED

def quiz():
    print("Welcome to the Python Knowledge Quiz!")
    
    # Questions and correct answers (fixed typos from original)
    questions = [
        "1. Which is NOT a Python data type?\nOptions: a) int, b) float, c) rational, d) string, e) bool",
        "2. Which is NOT a built-in Python operation?\nOptions: a) +, b) %, c) abs(), d) sqrt()",
        "3. In mixed int/float expressions, Python converts:\nOptions: a) float to int, b) int to string, c) both to string, d) int to float",
        "4. Best structure for multi-way decisions?\nOptions: a) if, b) if-else, c) if-elif-else, d) try",
        "5. Which statement immediately terminates a loop?\nOptions: a) if, b) exit, c) continue, d) break"
    ]
    
    answers = ["c", "d", "d", "c", "d"]  # Correct answer letters
    score = 0                             # Initialize score counter

    # Quiz loop
    for i in range(len(questions)):
        user_answer = input(questions[i] + "\nYour choice (a/b/c/d/e): ").strip().lower()
        
        if user_answer == answers[i]:
            print("Correct!")
            control_led(True)    # Green LED for correct
            score += 1
        else:
            print("Incorrect!")
            control_led(False)   # Red LED for incorrect

    # Cleanup and results
    GPIO.cleanup()               # Reset GPIO pins
    print(f"\nFinal Score: {score}/{len(questions)}")

# Main program execution
if __name__ == "__main__":
    quiz()
