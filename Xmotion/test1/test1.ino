#include <xmotion.h>
int UserLed1 = 8; //Led1 Pin is D8
int UserLed2 = 9;
float sensorL = 0;
float sensorM = 0;
float sensorR = 0;

void setup() {
  pinMode(UserLed1, OUTPUT); // Led as output element
  Serial.begin(115200);
}
//void loop() {
//  digitalWrite(UserLed1, HIGH); // turn on the User Led 1, High Statement
//  delay(500); // wait for half second (500 ms)
//  digitalWrite(UserLed1, LOW); // turn off the User Led 1, Low Statement
//  delay(500); // wait for half second (500 ms)
//}

void loop() {
//  sensor1 = analogRead(1);
//  digitalWrite(UserLed1, HIGH); // turn on the User Led 1, High Statement
//  delay(int(sensor1*0.2)); // wait for half second (500 ms)
//  digitalWrite(UserLed1, LOW); // turn off the User Led 1, Low Statement
//  delay(int(sensor1*0.2)); // wait for half second (500 ms)
  sensorL = analogRead(2);
  sensorM = analogRead(4);
  sensorR = analogRead(1);
//  if (sensor>700){
//    digitalWrite(UserLed1, HIGH);
//  }else{
//    digitalWrite(UserLed1, LOW);
//  }
//  digitalWrite(UserLed1, HIGH); // turn on the User Led 1, High Statement
//  delay(int(sensor*0.5)); 
//  digitalWrite(UserLed1, LOW); // turn off the User Led 1, Low Statement
//  delay(int(sensor*0.5)); 
  Serial.print(sensorL);
  Serial.print("\t");  
  Serial.print(sensorM);
  Serial.print("\t");
  Serial.print(sensorR);
  Serial.println(" ");
  
}
