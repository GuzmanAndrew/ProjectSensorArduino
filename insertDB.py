import mysql.connector
import serial
import time

connection = mysql.connector.connect(user="root", password="Andrewseigokan9*",
                                          host="localhost", port="3306",
                                          database="proyectnasa")

if connection.is_connected():
   print('Connect Successfully')
   connection_cursor = connection.cursor()
   arduino = serial.Serial('com13', 9600)
   while True:
      time.sleep(2)
      print('Established serial connection to Arduino')
      arduino_data = arduino.readline()
      unique_data = arduino_data.split(",")
      decode_humidity = int(unique_data[0].decode("utf-8"))
      decode_temp_c = int(unique_data[1].decode("utf-8"))
      decode_temp_f = int(unique_data[2].decode("utf-8"))
      print("HUMIDITY: " + decode_humidity)
      print("TEMPERATURE CELSIUS: " + decode_temp_c)
      print("TEMPERATURE FAHRENHEIT: " + decode_temp_f)
      sql = "INSERT INTO datasensor (humidity, temp_c, temp_f) VALUES (%s, %s, %s)"
      val = (decode_humidity, decode_temp_c, decode_temp_f)
      connection_cursor.execute(sql, val)

      connection.commit()

      print(connection_cursor.rowcount, "registro insertado")                                    