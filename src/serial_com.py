import serial

#neopixel HSV uses 16-bit int
#see HSV section on: https://learn.adafruit.com/adafruit-neopixel-uberguide/arduino-library-use
HUE_RANGE = 65536
HUE_MAGIC_NUM = 0.50 # cuts at half of the hue range, this allows blue -> red coloring for temperature smoothly
MIN_HUE = 0
MAX_HUE = int(HUE_RANGE * HUE_MAGIC_NUM)

def map_range(value_curr, min_curr, max_curr, min_new, max_new):
    range_curr = max_curr-min_curr
    range_new = max_new-min_new

    value_norm = (value_curr - min_curr) / (range_curr)
    return min_new + (value_norm*range_new)

def map_range_inv(value_curr, min_curr, max_curr, min_new, max_new):
    range_curr = max_curr-min_curr
    value_diff = value_curr - min_curr

    value_curr = max_curr - value_diff

    return map_range(value_curr, min_curr, max_curr, min_new, max_new)

class WeatherSerial():
    def __init__(self, com_port, baudrate=9600, timeout=.1):
        self.arduino = serial.Serial(com_port, baudrate=baudrate, timeout=timeout)

        #threshold for temperatures (celcius)
        self.temp_min_thres = 0
        self.temp_max_thres = 40
        self.interval = 2

    def temp_to_hues(self, temp):
        self.hues = [0,0]
        
        hue_hot = temp+self.interval
        hue_cold = temp-self.interval

        if hue_cold < self.temp_min_thres:
            hue_cold = self.temp_min_thres
            hue_hot = self.temp_min_thres + self.interval
        
        elif hue_hot > self.temp_max_thres:
            hue_hot = self.temp_max_thres
            hue_cold = self.temp_max_thres - self.interval


        self.hues[0] = int(map_range_inv(hue_hot, self.temp_min_thres, self.temp_max_thres, MIN_HUE, MAX_HUE))
        self.hues[1] = int(map_range_inv(hue_cold, self.temp_min_thres, self.temp_max_thres, MIN_HUE, MAX_HUE))
    
    def write_temp(self, temp, blink=0):
        self.temp_to_hues(temp)
        self.arduino.write(bytes(f"{self.hues[0]},{self.hues[1]},{blink}",'utf-8'))