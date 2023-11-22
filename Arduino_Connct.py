import serial                                                              
import time                                                                
ArduinoUnoSerial = serial.Serial('com15',9600)       
print(ArduinoUnoSerial.readline())                           
print ("You have new message from Arduino")
while 1:
    #declare var=1 if the posture is wrong else declare var=0                                                  
    if (var == '1'):
        ArduinoUnoSerial.write('1')                                 
        time.sleep(1)
    if (var == '0'):
        ArduinoUnoSerial.write('0')
        time.sleep(1)
 
'''int data;
int LED=13;
Int buzzer=12;
void setup() { 
  Serial.begin(9600);                             
  pinMode(LED, OUTPUT);
     pinMode(buzzer, OUTPUT);                
  digitalWrite (LED, LOW);                      
  
}
void loop() {
while (Serial.available())   
{ 
data = Serial.read();
}
if (data == '1')
digitalWrite (LED, HIGH); 
tone(buzzer,500);              
else if (data == '0')
digitalWrite (LED, LOW);  
notone(buzzer);            
}'''

#Link for Online Arduino Simulation
#https://www.tinkercad.com/things/4IfETsRBeJW-posture-detection/editel?sharecode=9H-FIBBhjB4WzJiWL_3goBcM3EDE-UODxQMQhbm2XII
