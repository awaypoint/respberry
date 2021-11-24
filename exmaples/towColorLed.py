import time

import RPi.GPIO as GPIO


class Button:
    button_pin = 19
    red_pin = 20
    green_pin = 16

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.red_pin, GPIO.OUT)
        GPIO.setup(self.green_pin, GPIO.OUT)

    def __del__(self):
        GPIO.output(self.red_pin, GPIO.LOW)
        GPIO.output(self.green_pin, GPIO.LOW)
        self.cleanup()

    def start(self):
        count = 1
        while True:
            button = GPIO.input(self.button_pin)
            if button == GPIO.HIGH:
                red_pin_value = GPIO.HIGH if count % 3 == 1 else GPIO.LOW
                green_pin_value = GPIO.HIGH if count % 3 == 2 else GPIO.LOW
                count += 1
                GPIO.output(self.red_pin, red_pin_value)
                GPIO.output(self.green_pin, green_pin_value)
                time.sleep(0.5)
            time.sleep(0.1)

    def cleanup(self):
        print("clean up")
        GPIO.output(self.red_pin, GPIO.LOW)
        GPIO.output(self.green_pin, GPIO.LOW)
        GPIO.cleanup()


if __name__ == '__main__':
    Button = Button()
    try:
        Button.start()
    except KeyboardInterrupt:
        print("exit")
