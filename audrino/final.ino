
define VRX_PIN A0 // X-axis
#define VRY_PIN A1 // Y-axis
#define SW_PIN 7  // Joystick button
#define TOUCH_SENSOR 9 
#include <LiquidCrystal.h>
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

unsigned long lastButtonTime = 0;
const int DEBOUNCE_DELAY = 50;

const unsigned int countdownTime = 1500; // 30 minutes in seconds
unsigned int remainingTime = countdownTime;
unsigned long previousMillis = 0;
bool timerRunning = false;
bool lastTouchState = LOW;

void setup() {
  Serial.begin(9600);
  pinMode(SW_PIN, INPUT_PULLUP);
  lcd.begin(16, 2);
  lcd.setCursor(0, 0);
  lcd.print("Touch to study");
  lcd.setCursor(0, 1);
  displayTime(remainingTime);
  
}

void loop() {
  unsigned long currentTime = millis();
  int y = analogRead(VRY_PIN);
  bool buttonPressed = !digitalRead(SW_PIN);
  if(y<300 || y>700){
    Serial.println(y);
  }
  if (buttonPressed && currentTime - lastButtonTime > DEBOUNCE_DELAY) {
    int button = !digitalRead(SW_PIN);
    Serial.println(button); // Send "1" when button is pressed
    lastButtonTime = currentTime;
  }
  delay(1000); // Adjust delay as needed

  bool touchState = digitalRead(TOUCH_SENSOR);

    // Check for touch state change
    if (touchState == HIGH && lastTouchState == LOW) {
        delay(50); // Debounce delay
        if (digitalRead(TOUCH_SENSOR) == HIGH) { // Confirm touch
            timerRunning = !timerRunning; // Toggle timer state
            if (timerRunning) {
                lcd.setCursor(0, 0);
                lcd.print("Timer Running ");
            } else {
                lcd.setCursor(0, 0);
                lcd.print("Timer Paused  ");
            }
        }
    }
    lastTouchState = touchState;

    if (timerRunning) {
        unsigned long currentMillis = millis();
        if (currentMillis - previousMillis >= 1000) { // Update every second
            previousMillis = currentMillis;
            if (remainingTime > 0) {
                remainingTime--;
                displayTime(remainingTime);
            } else {
                timerRunning = false;
                lcd.setCursor(0, 0);
                lcd.print("Time's Up!");
            }
        }
    }

  delay(200);
}

void displayTime(unsigned int timeInSeconds) {
    unsigned int minutes = timeInSeconds / 60;
    unsigned int seconds = timeInSeconds % 60;

    lcd.setCursor(0, 1);
    lcd.print("Time: ");
    if (minutes < 10) lcd.print('0');
    lcd.print(minutes);
    lcd.print(':');
    if (seconds < 10) lcd.print('0');
    lcd.print(seconds);
    lcd.print("  "); // Clear any extra characters
}

 
