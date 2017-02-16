import RPi.GPIO as GPIO

from rpilike import RPiLikePlatform


class FishpiPlatform(RPiLikePlatform):

	def __init__(self, config):
		super(RaspberrypiPlatform, self).__init__(config, 'fishpi', GPIO)

	def setup(self):
		GPIO.setwarnings(False)
		GPIO.cleanup()
		GPIO.setmode(GPIO.BCM)

		super(RaspberrypiPlatform, self).setup()
