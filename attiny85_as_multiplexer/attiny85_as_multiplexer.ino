int multi1 = 13;
int multi2 = 12;
int multi3 = 11;
int start = 10;
void setup()
{
pinMode(multi1, OUTPUT);
pinMode(multi2, OUTPUT);
pinMode(multi3, OUTPUT);
pinMode(start, INPUT);
}
void loop()
{
  while(start == HIGH){
    digitalWrite(multi1, HIGH);
    delayMicroseconds(1);
    digitalWrite(multi1, LOW);
    digitalWrite(multi2, HIGH);
    delayMicroseconds(1);
    digitalWrite(multi2, LOW);
    digitalWrite(multi3, HIGH);
    delayMicroseconds(1);
    digitalWrite(multi3, LOW);
  }
}
