int led = 13;

String command; 

void setup() {                
  // initialize the digital pin as an output.
  Serial.begin(9600);
  pinMode(led, OUTPUT);   

}

// the loop routine runs over and over again forever:
void loop() {

  if(Serial.available()){

    command = Serial.readStringUntil("\n");
    command.trim();
    if (command.equals("on")){
        Serial.println("ON");
        digitalWrite(led, HIGH);   // turn the LED on (HIGH is the voltage level)
        delay(2000);               // wait for a second
        
    }
    if (command.equals("off")){
        Serial.println("OFF");
        digitalWrite(led, LOW);   // turn the LED on (HIGH is the voltage level)
        delay(2000);               // wait for a second

  }

}
}
