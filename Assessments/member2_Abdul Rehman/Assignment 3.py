from gpiozero import Button, TrafficLights, Buzzer    
from time import sleep    
    
buzzer = Buzzer(21)    
button = Button(15)    
lights = TrafficLights(25, 8, 7)    
    
while True:
  #isbutton pressed
  button.wait_for_press() 
  #turn on buzzer
  buzzer.on()   
  #turn on amber led
  lights.amber.on()  
  #delay
  sleep(3)    
  #turn on red led
  lights.red.on()    
  sleep(3)
  #turn on green led
  lights.green.on()
  sleep(3)  
  #turn off all
  lights.off()   
  buzzer.off()