#include <Adafruit_NeoPixel.h>

//neopixel variable
#define LED_PIN     6 
#define LED_COUNT   4

// Declare our NeoPixel strip object:
Adafruit_NeoPixel strip(LED_COUNT, LED_PIN, NEO_GRB + NEO_KHZ800);

int hueMin;
int hueMax;
bool blink;

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(1);

  strip.begin();           // INITIALIZE NeoPixel strip object (REQUIRED)
  strip.show();            // Turn OFF all pixels ASAP
  strip.setBrightness(50); // Set BRIGHTNESS to about 1/5 (max = 255)
}

void loop() {
  while(!Serial.available());
  hueMin = Serial.readStringUntil(',').toInt();
  hueMax = Serial.readStringUntil(',').toInt();
  blink = Serial.readStringUntil('\n').toInt();
  
  Serial.print("HueMin: ");
  Serial.println(hueMin);

  Serial.print("HueMax: ");
  Serial.println(hueMax);

  setStripColor(hueMin, hueMax);

  strip.show();
  
  if(blink) {
    for(int i=0; i<5; i++) {
      delay(500);
      strip.setBrightness(5);
      strip.show();
      delay(500);
      strip.setBrightness(50);
      strip.show();
    }
  }
}

void setStripColor(int hueMin, int hueMax) {
  int hue;
  uint32_t rgbcolor;
  for(int i=0; i<strip.numPixels(); i++) { // For each pixel in strip...
    hue = (int) hueMin + i*((hueMax-hueMin)/(LED_COUNT-1));
    rgbcolor = strip.ColorHSV(hue);
    strip.setPixelColor(i, rgbcolor);         //  Set pixel's color (in RAM)
  }
}
