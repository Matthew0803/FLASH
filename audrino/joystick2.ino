#define VRX_PIN A0 // X-axis
#define VRY_PIN A1 // Y-axis
#define SW_PIN 7   // Joystick button

// Define thresholds for movement and debouncing
const int MOVEMENT_THRESHOLD = 200;  // Adjust as needed
const int DEBOUNCE_DELAY = 500; // milliseconds

// Variables to store previous readings and times
int prevXValue = 512; // Initialize to center
int prevYValue = 512; // Initialize to center
unsigned long lastXTime = 0;
unsigned long lastYTime = 0;
unsigned long lastButtonTime = 0;

// Variables to track joystick state
enum JoystickState { CENTER, LEFT, RIGHT, UP, DOWN };
JoystickState currentXState = CENTER;
JoystickState currentYState = CENTER;

// Variable to store the selected option (A, B, C, or D)
char selectedOption = ' '; // Initialize to a space

void setup() {
  pinMode(SW_PIN, INPUT_PULLUP);
  Serial.begin(9600);
}

void loop() {
  int xValue = analogRead(VRX_PIN);
  int yValue = analogRead(VRY_PIN);
  bool buttonPressed = !digitalRead(SW_PIN); // LOW when pressed

  unsigned long currentTime = millis();

  // Handle X-axis (LEFT/RIGHT) for option selection
  if (abs(xValue - prevXValue) > MOVEMENT_THRESHOLD && currentTime - lastXTime > DEBOUNCE_DELAY) {
    if (xValue < 512 && currentXState != LEFT) { // Left
      selectedOption = 'A';
      currentXState = LEFT;
      Serial.println(selectedOption); // Send selected option
    } else if (xValue > 512 && currentXState != RIGHT) { // Right
      selectedOption = 'B';
      currentXState = RIGHT;
      Serial.println(selectedOption); // Send selected option
    }
    prevXValue = xValue;
    lastXTime = currentTime;
  } else if (abs(xValue - 512) < MOVEMENT_THRESHOLD && currentXState != CENTER) { // Back to center
    currentXState = CENTER;
    selectedOption = ' '; // Reset selected option
  }

  // Handle Y-axis (UP/DOWN) for option selection (C and D)
  if (abs(yValue - prevYValue) > MOVEMENT_THRESHOLD && currentTime - lastYTime > DEBOUNCE_DELAY) {
    if (yValue < 512 && currentYState != UP) { // Up
      selectedOption = 'C';
      currentYState = UP;
      Serial.println(selectedOption); // Send selected option
    } else if (yValue > 512 && currentYState != DOWN) { // Down
      selectedOption = 'D';
      currentYState = DOWN;
      Serial.println(selectedOption); // Send selected option
    }
    prevYValue = yValue;
    lastYTime = currentTime;
  } else if (abs(yValue - 512) < MOVEMENT_THRESHOLD && currentYState != CENTER) { // Back to center
    currentYState = CENTER;
    selectedOption = ' '; // Reset selected option
  }

  // Handle button press (SELECT) to submit answer
  if (buttonPressed && currentTime - lastButtonTime > DEBOUNCE_DELAY) {
    if (selectedOption != ' ') { // Only send if an option is selected
      Serial.println(selectedOption); // Send the selected option again to confirm
      Serial.println("SUBMIT"); // Send "SUBMIT" to indicate submission
      selectedOption = ' '; // Reset selected option after submission
    }
    lastButtonTime = currentTime;
  }

  delay(50); // Adjust as needed
}