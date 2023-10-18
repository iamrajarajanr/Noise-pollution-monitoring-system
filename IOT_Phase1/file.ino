
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2); // Set the LCD address and dimensions

const int soundSensorPin = A0; // Analog pin for the sound sensor
int noiseValue = 0;

void setup() {
  lcd.init(); // Initialize the LCD
  lcd.backlight(); // Turn on the backlight

  Serial.begin(9600); // Initialize serial communication
}

void loop() {
  noiseValue = analogRead(soundSensorPin); // Read the analog value from the sound sensor
  float noiseLevel = (noiseValue * 5.0) / 1023.0; // Convert analog value to voltage

  // Display noise level on LCD
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Noise Level:");
  lcd.setCursor(0, 1);
  lcd.print(noiseLevel);
  lcd.print(" V");

  // Print noise level to serial monitor
  Serial.print("Noise Level: ");
  Serial.print(noiseLevel);
  Serial.println(" V");

  delay(1000); // Delay for a second before taking the next reading
}
