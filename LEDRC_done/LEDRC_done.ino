#include <Tlc5940.h>
/*
Scott Harwood, LED Rubik's Cube Project
The project was to make a working LED rubik's cube on arduino and RPi
*/
//include the Tlc5940 lib for the Ti Tlc5940 ic
  int RED = 0;
  int GREEN = 0;
  int BLUE = 0;
  int ORANGE = 0;
 int LED_num = 0; 
void setup()//setup
{
  Serial.begin(9600);//open serial port at baudrate:9600
  Tlc.init(4095);
}
void loop()//loop
{
  while(Serial.available() == '0');
  while(LED_num != 53){
    int LED_color = Serial.read() - '0';  
    if( LED_color == '0')// "0" = RED
    {
      Tlc.set(LED_num, RED);//LED_num = red pin of led 
    }
    else if (LED_color == '1')// "1" = GREEN
    {
       Tlc.set(LED_num + 1, GREEN);// LED_num + 1 = green pin of led
    }
    else if (LED_color == '2')//"2" = BLUE
    {
      Tlc.set(LED_num + 2, BLUE); //LED_num + 2 = blue pin of led
    }
    else if (LED_color == '3')//"3" = WHITE
    {
     Tlc.set(LED_num, RED);
     Tlc.set(LED_num + 1, GREEN);
     Tlc.set(LED_num + 2, BLUE);
    }
    else if (LED_color == '4')//"4" = YELLOW
    {
    Tlc.set(LED_num, RED);
    Tlc.set(LED_num + 1, GREEN);
    }
    else if (LED_color == '5')//"5" = orange
    {
    Tlc.set(LED_num, RED);
    Tlc.set(LED_num, ORANGE); 
    }
 if (LED_num == '53')
 {
   int LED_num = '0';
   Tlc.update();
 }
 else
 {
   int LED_num = LED_num + 3;
 }
}
}
