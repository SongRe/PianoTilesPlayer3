#include <Servo.h>
Servo motor1, motor2, motor3, motor4;
int MOTOR_PIN_1 = 12;
int MOTOR_PIN_2 = 11;
int MOTOR_PIN_3 = 10;
int MOTOR_PIN_4 = 9;

int up = 80;
int down = 100;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  motor1.attach(MOTOR_PIN_1);
  motor1.write(up);

  motor2.attach(MOTOR_PIN_2);
  motor2.write(up);

  motor3.attach(MOTOR_PIN_3);
  motor3.write(up);

  motor4.attach(MOTOR_PIN_4);
  motor4.write(up);
}

void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');
    //Receive tap downs
     if (data[0] == '1' ) {
      motor1.write(down);
      delay(75);
      motor1.write(up);
      Serial.println("1");
    }
    if (data[1] == '1') {
      motor2.write(down);
      delay(75);
      motor2.write(up);
      Serial.println("2");
    }
    if (data[2] == '1') {
      motor3.write(down);
      delay(75);
      motor3.write(up);
      Serial.println("3");
    }
    if (data[3] == '1') {
      motor4.write(down);
      delay(75);
      motor4.write(up);
      Serial.println("4");
    }
    //Receive tap ups
//    else if (data == "10") {
//      motor1.write(0);
//    }
//    else if (data == "20") {
//      motor2.write(0);
//    }
//    else if (data == "30") {
//      motor3.write(0);
//    }
//    else if (data == "40") {
//      motor4.write(0);
//    }
  }
}
