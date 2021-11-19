# code by chris-gong source from https://github.com/chris-gong/forty-yard-dash-rpi/blob/master/photoResistorTest.py
import RPi.GPIO as GPIO
import time

def data_collection():
    GPIO.setmode(GPIO.BOARD)

    resistorPin = 7


    GPIO.setup(resistorPin, GPIO.OUT)
    GPIO.output(resistorPin, GPIO.LOW)
    time.sleep(0.1)
    
    GPIO.setup(resistorPin, GPIO.IN)
    currentTime = time.time()
    diff = 0
    
    while(GPIO.input(resistorPin) == GPIO.LOW):
        diff  = time.time() - currentTime
        
    data1 = diff * 1000
    # print("original:{}".format(data1))
    print('put your paper on')
    time.sleep(3)
    

    GPIO.setup(resistorPin, GPIO.OUT)
    GPIO.output(resistorPin, GPIO.LOW)
    time.sleep(0.1)
    
    GPIO.setup(resistorPin, GPIO.IN)
    currentTime = time.time()
    diff = 0
    
    while(GPIO.input(resistorPin) == GPIO.LOW):
        diff  = time.time() - currentTime
        
    data2 = diff * 1000
    # print("filtered:{}".format(data2))

    # with open("sketching_paper.txt","a") as dt:
    #     dt.write(str(data1)+" "+str(data2)+"\n") 
    # time.sleep(5)
    return {"Orginal":data1,"Filted":data2}

if __name__ =="__main__":
    data_collection()