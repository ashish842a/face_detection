from pyfirmata import Arduino, OUTPUT, util
import time

PORT = "COM8"  # Adjust this to the correct COM port
pin = 10

board = Arduino(PORT)

# Define servo pin as an OUTPUT
board.digital[pin].mode = OUTPUT

def rotateServo(pin, angle):
    # Map the angle value to servo pulse width range (500-2500)
    pulse_width = int(angle / 180 * 2000) + 500
    board.digital[pin].write(pulse_width)

def doorAutomate(val):
    if val == 0:
        # Rotate the servo to open the door
        rotateServo(pin, 0)  # Adjust angle as needed
    elif val == 1:
        # Rotate the servo to close the door
        rotateServo(pin, 180)  # Adjust angle as needed

# Main function
if __name__ == "__main__":
    # Wait for the board to initialize
    time.sleep(2)

    # Perform door automation
    doorAutomate(0)  # Open the door

    # Delay to keep the door open for a certain duration
    time.sleep(5)  # Adjust the duration as needed

    # Close the door
    doorAutomate(1)

    # Release resources
    board.exit()
