char dataString[50] = {0};
int a =0; 
int b =0;
int c=0;
void setup() {
Serial.begin(9600);
Serial2.begin(14400); //Starting serial communication
}
  
void loop() {
  a++;                          // a value increase every loop
  sprintf(dataString,"%02X",a); // convert a value to hexa 
  Serial.println(dataString);   // send the data
  delay(1000);
  b++;
  c=c+b;
  Serial2.println(c);   // send the data
                                 // give the loop some break
}
