import RPi.GPIO as GPIO
import time
import requests

def main():
# initialise a previous input vaiable to 0 (assume button not pressed last)
prev_input = 0

# init GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.OUT, initial=0)
GPIO.setup(24, GPIO.OUT, initial=0)
GPIO.setup(25, GPIO.OUT, initial=0)

#set up the third GPIO just like above ^^^


prev_input = 1

while True:

    #INPUT 1
    # take a reading
    input1 = GPIO.input(17)
    # if the last reading was low and this one high, print
    if ((not prev_input) and input1):
        post('1')
        print("Button pressed") + '1'
    # update previous input
    prev_input = input1
    time.sleep(0.05)

    #INPUT 2
    input2 = GPIO.input(18)
    # if the last reading was low and this one high, print
    if ((not prev_input) and input2):
        post('2')
        print("Button pressed") + '2'
    # update previous input
    prev_input = input2
    time.sleep(0.05)

    # INPUT 3
        input3 = GPIO.input(19)
    # if the last reading was low and this one high, print
    if ((not prev_input) and input3):
         post('3')
         print("Button pressed") + '3'
    # update previous input
            prev_input = input3
    time.sleep(0.05)
def turnOnLED(led_id):
if (led_id == "1"):
GPIO.output(23, 1)
GPIO.output(24, 0)
GPIO.output(25, 0)
print('led 1 on')
if (led_id == "2"):
GPIO.output(23, 0)
GPIO.output(24, 1)
GPIO.output(25, 0)
print('led 2 on')
if (led_id == "3"):
GPIO.output(23, 0)
GPIO.output(24, 0)
GPIO.output(25, 1)
print('led 3 on')

def post(button_id):
#payload dict - sent to sever in next line. if you want to add a keyvalue, just follow below.
payload = {'raspi_id': getserial(), 'button_id': button_id}
print payload

#post the request to the server, but .get to save time.
#r = requests.post("http://requestb.in/17xxmyh1", data=payload)
r = requests.get("http://socialelder.meteor.com/request/222/3", data=payload)
turnOnLED(button_id)
return r

def getserial():
# Extract serial from cpuinfo file
cpuserial = "0000000000000000"
try: f = open('/proc/cpuinfo','r')
for line in f: if line[0:6]=='Serial':
cpuserial = line[10:26]
f.close()
except: cpuserial = "ERROR000000000"

return cpuserial
if name == "main":
main()
