#define VRX_PIN A0 // X-axis
#define VRY_PIN A1 // Y-axis
#define SW_PIN 7   // Joystick button

void setup() {
  pinMode(SW_PIN, INPUT_PULLUP);
  Serial.begin(9600);
}

void loop() {
  int xValue = analogRead(VRX_PIN);
  int yValue = analogRead(VRY_PIN);
  bool buttonPressed = !digitalRead(SW_PIN); // LOW when pressed

  // Define thresholds for movement
  int threshold = 300;
  if (xValue < threshold) {
    Serial.println("LEFT");
    delay(500);
  } else if (xValue > 1023 - threshold) {
    Serial.println("RIGHT");
    delay(500);
  }

  if (yValue < threshold) {
    Serial.println("UP");
    delay(500);
  } else if (yValue > 1023 - threshold) {
    Serial.println("DOWN");
    delay(500);
  }

  if (buttonPressed) {
    Serial.println("SELECT");
  }
  bool ou5  while(buttonPressed){
    Serial.println("SELECT");
  }
  

  delay(100); // Adjust as needed
}

