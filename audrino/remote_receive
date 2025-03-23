#include <IRremote.h>

const int RECV_PIN = 2;  // Change to the pin where your IR receiver is connected
IRrecv irrecv(RECV_PIN);
decode_results results;

void setup() {
  Serial.begin(9600);
  irrecv.enableIRIn(); // Start the IR receiver
  Serial.println("IR Receiver Test - Press any button on the remote");
}

void loop() {
  if (irrecv.decode(&results)) {
    Serial.print("Received IR Code: ");
    Serial.print(results.value, HEX);  // Print the code in HEX format
    Serial.print(" (Decimal: ");
    Serial.print(results.value, DEC);  // Print the code in Decimal format
    Serial.println(")");
    
    irrecv.resume(); // Resume receiving the next IR signal
  }
}
