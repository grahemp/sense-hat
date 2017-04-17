from sense_hat import *

sense = SenseHat()

# print(sense.temp)

humidity = sense.get_humidity()
print("Humidity: %s %%rH" % humidity)

Ctemp = sense.get_temperature()
Ftemp = 9.0/5.0 * Ctemp + 32
print("Temperature: %s F" % Ftemp)

# myfile = open('weather.txt', 'a')
# myfile.write(sense.temp)
# myfile.write('\n')
# myfile.close()

