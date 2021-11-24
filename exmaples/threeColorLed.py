import time

import RPi.GPIO as GPIO


class Button:
    button_pin = 19
    red_pin = 20
    green_pin = 16
    blue_pin = 12
    pin_list = [red_pin, green_pin, blue_pin]

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        for pin in self.pin_list:
            GPIO.setup(pin, GPIO.OUT)

    def __del__(self):
        self.set_pin_value()
        GPIO.cleanup()

    def set_pin_value(self, high_pin=[]):
        for pin in self.pin_list:
            value = GPIO.HIGH if pin in high_pin else GPIO.LOW
            GPIO.output(pin, value)

    def start(self):
        count = 1
        while True:
            button = GPIO.input(self.button_pin)
            if button == GPIO.HIGH:
                mod = count % 4
                dist = {
                    0: [],
                    1: [self.red_pin],
                    2: [self.green_pin],
                    3: [self.blue_pin],
                }
                self.set_pin_value(dist[mod])
                count += 1
                time.sleep(0.5)
            time.sleep(0.1)


if __name__ == '__main__':
    Button = Button()
    try:
        Button.start()
    except KeyboardInterrupt:
        print("exit")
