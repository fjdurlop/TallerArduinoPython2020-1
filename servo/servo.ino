 // Incluímos la librería para poder controlar el servo
#include <Servo.h>;
int pos;
String inByte;
 int SerialSpeed1 ;                
 int SerialSpeed2 ;                
 int SerialSpeed3 ;             
 int  SerialTotal = ((SerialSpeed3) + (SerialSpeed2*10) + SerialSpeed1*100); 
// Declaramos la variable para controlar el servo
Servo servoMotor;
 int estado;
void setup() {
  // Iniciamos el monitor serie para mostrar el resultado
  Serial.begin(9600);
 
  // Iniciamos el servo para que empiece a trabajar con el pin 9
  servoMotor.attach(9);
}
 
void loop() {
  
 
  while(Serial.available() > 0) {
    inByte = Serial.readStringUntil('\n'); // read data until newline
    pos = inByte.toInt();   // change datatype from string to integer        
   
     servoMotor.write(pos);
     Serial.print("Servo in position: ");  
    Serial.println(inByte);
    //Serial.println(estado);
  }//del if
}
