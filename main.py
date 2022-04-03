import serial
import time
import schedule

def main_func():
    arduino = serial.Serial('com13', 9600)
    print('Established serial connection to Arduino')
    arduino_data = arduino.readline()

    decoded_values = str(arduino_data[0:len(arduino_data)].decode("utf-8"))
    list_values = decoded_values.split(',')

    for item in list_values:
      list_in_floats.append(item)

    print(f'Data Humidity: {list_in_floats}')
    # print(f'Data Temperature Celsius: {list_in_floats[1]}')
    # print(f'Data Temperature Fahrenheit : {list_in_floats[2]}')

    arduino_data = 0
    list_in_floats.clear()
    list_values.clear()
    arduino.close()
    print('Connection closed')
    print('<----------------------------->')


# ----------------------------------------Main Code------------------------------------
# Declare variables to be used
list_values = []
list_in_floats = []

print('Program started')

# Setting up the Arduino
schedule.every(10).seconds.do(main_func)

while True:
    schedule.run_pending()
    time.sleep(1)