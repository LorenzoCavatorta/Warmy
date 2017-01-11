char relay_status;

void setup() {
  Serial.begin(9600);
  for(char i=0;i<10;i++)
      pinMode(i, OUTPUT);
}

void loop() {
  //int test = digitalRead(6);
  char test = char('t');
  Serial.println(test);
  delay(1000);
}

void serialEvent() {
  if (Serial.available()) {
    char inChar = (char)Serial.read(); 
    inChar-='0';
    for(char i=0;i<10;i++)
      digitalWrite(i, LOW);
      relay_status = 'off';
    digitalWrite(inChar,HIGH);
  }
} 