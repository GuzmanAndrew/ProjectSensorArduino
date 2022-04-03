#include <DHT.h>
#include <DHT_U.h>

#define Type DHT11
int dhtPin = 2;
DHT HT(dhtPin, Type);
int humidity;
float tempC;
float tempF;
int dt = 750;

void setup(){
  Serial.begin(9600);
  HT.begin();
}

void loop(){
  humidity = HT.readHumidity();
  tempC = HT.readTemperature();
  tempF = HT.readTemperature(true);

  Serial.print(humidity);
  Serial.print(", ");
  Serial.print(tempC);
  Serial.print(", ");
  Serial.print(tempF);
  delay(dt);
}
