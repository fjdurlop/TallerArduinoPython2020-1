#include <Servo.h>
Servo myservo; 
String inByte;
int pos;

void setup() {
 
  myservo.attach(9); //Relaciona el pin 9 al servo
  Serial.begin(9600);
}

void loop()
{    
  if(Serial.available())  // if data available in serial port
    { 
    inByte = Serial.readStringUntil('\n'); // read data until newline
    pos = inByte.toInt();   // change datatype from string to integer        
    myservo.write(pos);     // move servo
    Serial.print("El servo esta en la posicion: ");  
    Serial.println(inByte);
    }
}
