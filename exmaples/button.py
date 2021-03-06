import time

import RPi.GPIO as GPIO


class Button:
    button_pin = 19
    led_pin = 20

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.led_pin, GPIO.OUT)

    def __del__(self):
        GPIO.output(self.led_pin, GPIO.LOW)
        self.cleanup()

    def start(self):
        light = False
        while True:
            button = GPIO.input(self.button_pin)
            if button == GPIO.HIGH:
                light = not light
                print(light)
                GPIO.output(self.led_pin, light)
                time.sleep(0.5)
            time.sleep(0.1)

    def cleanup(self):
        print("clean up")
        GPIO.output(self.led_pin, GPIO.LOW)
        GPIO.cleanup()


if __name__ == '__main__':
    Button = Button()
    try:
        Button.start()
    except KeyboardInterrupt:
        print("exit")
