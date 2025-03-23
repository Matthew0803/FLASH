#include <LiquidCrystal.h>

// Define the Arduino pins connected to the LCD
const int rs = 7, en = 8, d4 = 9, d5 = 10, d6 = 11, d7 = 12;

// Initialize the LCD library with the specified pins
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

const int soundSensorPin = A0; // Analog pin connected to the sound sensor
const int threshold = 500;     // Noise level threshold (adjust as needed)
const int referenceVoltage = 20;

void setup() {
  lcd.begin(16, 2); // Initialize the LCD with 16 columns and 2 rows
  lcd.print("Noise Level:");
}

void loop() {
  float sensorValue = analogRead(soundSensorPin);

  lcd.setCursor(0, 1); // Move to the second line
  lcd.print("Value: ");
  lcd.print(sensorValue);

  if (sensorValue > threshold) {
    lcd.setCursor(0, 1);
    lcd.print("Too Loud!       "); // Clear any leftover characters
  }
  delay(500); // Adjust the delay as needed
}
