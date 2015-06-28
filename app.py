import RPi.GPIO as GPIO
import time
import requests


def main():
	# initialise a previous input vaiable to 0 (assume button not pressed last)
	prev_input = 0
	url = "http://requestb.in/rf5ksirf"

	GPIO.setmode(GPIO.BCM)
	GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

	prev_input = 0
	while True:

		# take a reading
		input1 = GPIO.input(17)
		# if the last reading was low and this one high, print
		if ((not prev_input) and input1):
			post('1')
			print("Button pressed") + '1'
		# update previous input
		prev_input = input1
		time.sleep(0.05)

		input2 = GPIO.input(18)
		# if the last reading was low and this one high, print
		if ((not prev_input) and input2):
			post('2')
			print("Button pressed") + '2'
		# update previous input
		prev_input = input2
		time.sleep(0.05)

		# input3 = GPIO.input(19)
		# # if the last reading was low and this one high, print
		# if ((not prev_input) and input3):
		# 	post('3')
		# 	print("Button pressed") + '3'
		# # update previous input
		# prev_input = input3
		# time.sleep(0.05)


def post(button_id):
	payload = {'raspi_id': getserial(), 'button_id': button_id}
	r = requests.post("http://requestb.in/17xxmyh1", data=payload)
	return r


def getserial():
	# Extract serial from cpuinfo file
	cpuserial = "0000000000000000"
	try:
		f = open('/proc/cpuinfo','r')
		for line in f:
			if line[0:6]=='Serial':
				cpuserial = line[10:26]
		f.close()
	except:
		cpuserial = "ERROR000000000"

	return cpuserial

if __name__ == "__main__":
	main()
