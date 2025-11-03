

import RPi.GPIO as GPIO
import time
import I2C_LCD_driver
from mfrc522 import SimpleMFRC522  # Assuming you're using the MFRC522 RFID module

# GPIO Pin assignments for Rows (L) and Columns (C) for the Keypad
L1 = 4
L2 = 17
L3 = 27
L4 = 22
C1 = 13
C2 = 19
C3 = 26
C4 = 21

# GPIO Pin for controlling the lock (e.g., connected to a relay or transistor)
LOCK_PIN = 18  # Adjust to the pin controlling the lock

# RFID Lock Control
reader = SimpleMFRC522()

# Set up the GPIO pins
GPIO.setmode(GPIO.BCM)

# Set up lock pin as output (for controlling lock)
GPIO.setup(LOCK_PIN, GPIO.OUT)
GPIO.output(LOCK_PIN, GPIO.LOW)  # Lock is initially closed

# Set rows as outputs, columns as inputs with pull-down resistors for the keypad
GPIO.setup(L1, GPIO.OUT)
GPIO.setup(L2, GPIO.OUT)
GPIO.setup(L3, GPIO.OUT)
GPIO.setup(L4, GPIO.OUT)
GPIO.setup(C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Initialize the LCD display using the I2C LCD driver
mylcd = I2C_LCD_driver.lcd()

# Character map for the keypad (this is a typical 4x4 matrix)
keypad = [
    ['1', '2', '3', 'A'],
    ['4', '5', '6', 'B'],
    ['7', '8', '9', 'C'],
    ['*', '0', '#', 'D']
]

# Predefined correct password
correct_password = "1234"  # Change this to your desired password

# Store entered password
entered_password = ""

# Function to scan a row and determine which key was pressed
def readLine(row, characters):
    GPIO.output(row, GPIO.HIGH)  # Set the row pin HIGH to check columns
    if GPIO.input(C1) == 1:
        return characters[0]
    elif GPIO.input(C2) == 1:
        return characters[1]
    elif GPIO.input(C3) == 1:
        return characters[2]
    elif GPIO.input(C4) == 1:
        return characters[3]
    return None

# Function to scan the entire keypad (rows and columns)
def scanKeypad():
    for row, characters in zip([L1, L2, L3, L4], keypad):
        key = readLine(row, characters)
        if key is not None:
            return key
    return None

# Function to unlock the lock
def unlock_lock():
    GPIO.output(LOCK_PIN, GPIO.HIGH)  # Unlock the lock (active high or low depending on your setup)
    mylcd.lcd_clear()
    mylcd.lcd_display_string("Lock Unlocked!", 1)
    time.sleep(5)  # Keep the lock open for 5 seconds
    GPIO.output(LOCK_PIN, GPIO.LOW)  # Lock the lock again

# Function to handle RFID unlocking
def unlock_lock_rfid():
    mylcd.lcd_clear()
    mylcd.lcd_display_string("Place RFID tag", 1)
    id, text = reader.read()
    mylcd.lcd_clear()
    mylcd.lcd_display_string(f"ID: {id}", 1)
    # Assuming a predefined ID for unlocking, e.g., ID 123456789
    if id == 123456789:  # Replace this with your RFID ID
        unlock_lock()
    else:
        mylcd.lcd_display_string("Access Denied", 1)
        time.sleep(2)

# Main loop for the keypad password entry
def main_loop():
    global entered_password
    while True:
        key = scanKeypad()
        if key:
            if key == "#":  # Submit password when "#" is pressed
                if entered_password == correct_password:
                    unlock_lock()
                else:
                    mylcd.lcd_clear()
                    mylcd.lcd_display_string("Wrong Password!", 1)
                    time.sleep(2)
                entered_password = ""  # Reset entered password after submission
            elif key == "*":  # Clear the entered password when "*" is pressed
                entered_password = ""
                mylcd.lcd_clear()
                mylcd.lcd_display_string("Password Cleared", 1)
                time.sleep(2)
            else:
                entered_password += key  # Append the pressed key to the entered password
                mylcd.lcd_clear()
                mylcd.lcd_display_string("Enter Password:", 1)
                mylcd.lcd_display_string(entered_password, 2)
            time.sleep(0.2)  # Small delay for debouncing

# Main execution starts here
try:
    while True:
        # Try scanning RFID for unlocking
        unlock_lock_rfid()  # RFID Unlocking attempt

        # Call the main loop to handle keypad password entry
        main_loop()

except KeyboardInterrupt:
    print("Program terminated by user.")
finally:
    GPIO.cleanup()  # Clean up GPIO to reset pins

New Version:
from gpiozero import Button
import I2C_LCD_driver
import RPi.GPIO as GPIO
import time
from mfrc522 import SimpleMFRC522  # Assuming you're using the MFRC522 RFID module

L1 = 4
L2 = 17
L3 = 27
L4 = 22
C1 = 13
C2 = 19
C3 = 26
C4 = 21
Lock1 = 20

GPIO.setmode(GPIO.BCM)
GPIO.setup(L1, GPIO.OUT)
GPIO.setup(L2, GPIO.OUT)
GPIO.setup(L3, GPIO.OUT)
GPIO.setup(L4, GPIO.OUT)
GPIO.setup(C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

mylcd = I2C_LCD_driver.lcd()

def readLine(line, characters):
    GPIO.output(line, GPIO.HIGH)
    if(GPIO.input(C1) == 1):
        return characters[0]
    if(GPIO.input(C2) == 1):
        return characters[1]
    if(GPIO.input(C3) == 1):
        return characters[2]
    if(GPIO.input(C4) == 1):
        return characters[3]

while True:  # This is the loop that will repeat
    # Your loop code should go here
    # Don't put import statements inside this loop.
    pass 
import RPi.GPIO as GPIO
import time
import I2C_LCD_driver
from mfrc522 import SimpleMFRC522  # Assuming you're using the MFRC522 RFID module


# GPIO Pin for controlling the lock (e.g., connected to a relay or transistor)
LOCK_PIN = 18  # Adjust to the pin controlling the lock

# RFID Lock Control
reader = SimpleMFRC522()

# Set up the GPIO pins
GPIO.setmode(GPIO.BCM)

# Set up lock pin as output (for controlling lock)
GPIO.setup(LOCK_PIN, GPIO.OUT)
GPIO.output(LOCK_PIN, GPIO.LOW)  # Lock is initially closed

# Set rows as outputs, columns as inputs with pull-down resistors for the keypad
GPIO.setup(L1, GPIO.OUT)
GPIO.setup(L2, GPIO.OUT)
GPIO.setup(L3, GPIO.OUT)
GPIO.setup(L4, GPIO.OUT)
GPIO.setup(C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Initialize the LCD display using the I2C LCD driver
mylcd = I2C_LCD_driver.lcd()

# Character map for the keypad (this is a typical 4x4 matrix)
keypad = [
    ['1', '2', '3', 'A'],
    ['4', '5', '6', 'B'],
    ['7', '8', '9', 'C'],
    ['*', '0', '#', 'D']
]

# Predefined correct password
correct_password = "1234"  # Change this to your desired password

# Store entered password
entered_password = ""

# Function to scan a row and determine which key was pressed
def readLine(row, characters):
    GPIO.output(row, GPIO.HIGH)  # Set the row pin HIGH to check columns
    if GPIO.input(C1) == 1:
        return characters[0]
    elif GPIO.input(C2) == 1:
        return characters[1]
    elif GPIO.input(C3) == 1:
        return characters[2]
    elif GPIO.input(C4) == 1:
        return characters[3]
    return None

# Function to scan the entire keypad (rows and columns)
def scanKeypad():
    for row, characters in zip([L1, L2, L3, L4], keypad):
        key = readLine(row, characters)
        if key is not None:
            return key
    return None

# Function to unlock the lock
def unlock_lock():
    GPIO.output(LOCK_PIN, GPIO.HIGH)  # Unlock the lock (active high or low depending on your setup)
    mylcd.lcd_clear()
    mylcd.lcd_display_string("Lock Unlocked!", 1)
    time.sleep(5)  # Keep the lock open for 5 seconds
    GPIO.output(LOCK_PIN, GPIO.LOW)  # Lock the lock again

# Function to handle RFID unlocking
def unlock_lock_rfid():
    mylcd.lcd_clear()
    mylcd.lcd_display_string("Place RFID tag", 1)
    id, text = reader.read()
    mylcd.lcd_clear()
    mylcd.lcd_display_string(f"ID: {id}", 1)
    # Assuming a predefined ID for unlocking, e.g., ID 123456789
    if id == 123456789:  # Replace this with your RFID ID
        unlock_lock()
    else:
        mylcd.lcd_display_string("Access Denied", 1)
        time.sleep(2)

# Main loop for the keypad password entry
def main_loop():
    global entered_password
    while True:
        key = scanKeypad()
        if key:
            if key == "#":  # Submit password when "#" is pressed
                if entered_password == correct_password:
                    unlock_lock()
                else:
                    mylcd.lcd_clear()
                    mylcd.lcd_display_string("Wrong Password!", 1)
                    time.sleep(2)
                entered_password = ""  # Reset entered password after submission
            elif key == "*":  # Clear the entered password when "*" is pressed
                entered_password = ""
                mylcd.lcd_clear()
                mylcd.lcd_display_string("Password Cleared", 1)
                time.sleep(2)
            else:
                entered_password += key  # Append the pressed key to the entered password
                mylcd.lcd_clear()
                mylcd.lcd_display_string("Enter Password:", 1)
                mylcd.lcd_display_string(entered_password, 2)
            time.sleep(0.2)  # Small delay for debouncing

# Main execution starts here
try:
    while True:
        # Try scanning RFID for unlocking
        unlock_lock_rfid()  # RFID Unlocking attempt

        # Call the main loop to handle keypad password entry
        main_loop()

except KeyboardInterrupt:
    print("Program terminated by user.")
finally:
    GPIO.cleanup()  # Clean up GPIO to reset pins

