class Switchable:
    def turn_on(self):
        pass
    
    def turn_off(self):
        pass

class LightBulb(Switchable):
    def turn_on(self):
        print("LightBulb: Turned On")
    
    def turn_off(self):
        print("LightBulb: Turned Off")

class Fan(Switchable):
    def turn_on(self):
        print("Fan: Turned On")
    
    def turn_off(self):
        print("Fan: Turned Off")

class Switch:
    def init(self, device: Switchable):
        self.device = device
    
    def operate(self, command):
        if command == "ON":
            self.device.turn_on()
        elif command == "OFF":
            self.device.turn_off()

light = LightBulb()
fan = Fan()

switch1 = Switch(light)
switch2 = Switch(fan)

switch1.operate("ON")
switch1.operate("OFF")

switch2.operate("ON")
switch2.operate("OFF")

