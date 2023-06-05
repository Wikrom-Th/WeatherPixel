#include <Adafruit_NeoPixel.h>

//neopixel variable
#define LED_PIN     6 
#define LED_COUNT   4

// Declare our NeoPixel strip object:
Adafruit_NeoPixel strip(LED_COUNT, LED_PIN, NEO_GRB + NEO_KHZ800);

int value; //read from serial

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(1);

  strip.begin();           // INITIALIZE NeoPixel strip object (REQUIRED)
  strip.show();            // Turn OFF all pixels ASAP
  strip.setBrightness(50); // Set BRIGHTNESS to about 1/5 (max = 255)
}

void loop() {
  while(!Serial.available());
  value = Serial.readString().toInt();
  Serial.print("Temp: ");
  Serial.print(value);


  if(value<0) {
    //white
    setStaticColor(strip.Color(255, 255, 255));
  }
  else if(value<=15) {
    //light blue
    setStaticColor(strip.Color(0,   153, 255));
  }
  else if(value<25) {
    //green
    setStaticColor(strip.Color(0,   255,   0));
  }
  else {
    //red
    setStaticColor(strip.Color(255,   0,   0));
  }
}

void setStaticColor(uint32_t color) {
  for(int i=0; i<strip.numPixels(); i++) { // For each pixel in strip...
    strip.setPixelColor(i, color);         //  Set pixel's color (in RAM)
  }
  strip.show();                          //  Update strip to match
}
