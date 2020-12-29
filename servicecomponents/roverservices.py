import RPi.GPIO as GPIO

class CoreServices:
    def __init__(self):
        self.message=''
        self.led_out=12
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.led_out, GPIO.OUT)

    def turnLightsOnOff(self,lightsOn=False):
        if lightsOn:
            GPIO.output(self.led_out,GPIO.HIGH)
        else:
            GPIO.output(self.led_out,GPIO.LOW)

    def headLightsOn(self,lightsOn=False):
        if lightsOn:
            self.message='Head lights Turned On!!!'
        else:
            self.message='Head lights Turned Off!!!'

        turnLightsOnOff(lightsOn)
        return self.message
    


            


        