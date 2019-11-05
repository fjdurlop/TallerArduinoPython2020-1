 // Incluímos la librería para poder controlar el servo
#include <Servo.h>;
int pos,posV;
String inByte;
 /*int SerialSpeed1 ;                
 int SerialSpeed2 ;                
 int SerialSpeed3 ;             
 int  SerialTotal = ((SerialSpeed3) + (SerialSpeed2*10) + SerialSpeed1*100); 
*/
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
    if(pos==1){
      posV=posV+30;
      servoMotor.write(posV);
      }
      else if(pos==0){
        posV=posV-30;
        servoMotor.write(posV);
        }
     else if(pos==2){
          for (posV = 0; posV <= 180; posV += 1) { // goes from 0 degrees to 180 degrees
          // in steps of 1 degree
            servoMotor.write(posV);              // tell servo to go to position in variable 'pos'
            delay(15);                       // waits 15ms for the servo to reach the position
          }
    }
     else if(pos==3){
        for (posV = 180; posV >= 0; posV -= 1) { // goes from 180 degrees to 0 degrees
          servoMotor.write(posV);              // tell servo to go to position in variable 'pos'
          delay(15);
        }
     }
     
     Serial.print("Servo in position: ");  
    Serial.println(String(posV));
    //Serial.println(estado);
  }//del if
}
