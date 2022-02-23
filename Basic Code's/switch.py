import RPi.GPIO as GPIO            
import time                      
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)         
GPIO.setup(18, GPIO.OUT)
GPIO.setup(12, GPIO.IN) 
while True:
    input_state = GPIO.input(12) 
    if (input_state == 1):     
       print("light is on")   
       GPIO.output(18, 1)  
    else:
        print("light is off")  
        GPIO.output(18, 0)
        
