
#include <DHT11.h>

int pin=3;
DHT11 dht11(pin);

int incomingByte = 0;   // for incoming serial data
// 0 - 48
// 1 - 49
// 2 - 50
// 3 - 51
float gas_value;
///////////mq2//////////
#define         MQ1                       (0)     //define la entrada analogica para el sensor

////////////////////////

///////////mq4//////////
#define         MQ4                       (1)     //define la entrada analogica para el sensor
////////////////////////

///////////mq5//////////
#define         MQ5                       (2)     //define la entrada analogica para el sensor
////////////////////////

///////////mq6//////////
#define         MQ6                       (3)     //define la entrada analogica para el sensor
////////////////////////

///////////mq7//////////
#define         MQ7                       (4)     //define la entrada analogica para el sensor
////////////////////////

///////////mq8//////////
#define         MQ8                       (5)     //define la entrada analogica para el sensor
////////////////////////

///////////mq135//////////
#define         MQ135                       (6)     //define la entrada analogica para el sensor
////////////////////////
int scan=52;
int valor=0;
void setup() {
        Serial.begin(9600);     // abre los puertos a 9600b
        pinMode(scan, INPUT); // configura botón (pin7) como entrada
}

void loop() {
       int err;
       float temp, hum;
      
          
          
        // send data only when you receive data:
        if (Serial.available() > 0) {
                // read the incoming byte:
                incomingByte = Serial.read();
                if(incomingByte==49){////////////////mq-2
                  gas_value=analogRead(MQ1);
                  Serial.println(gas_value);       
                }
                
                if(incomingByte==50){////////////////mq-4
                  gas_value=analogRead(MQ4);
                  Serial.println(gas_value);
                }
                if(incomingByte==51){///////////////////mq-5
                  gas_value=analogRead(MQ5);
                  Serial.println(gas_value);
                }
                if(incomingByte==52){///////////mq-6
                  gas_value=analogRead(MQ6);
                  Serial.println(gas_value);
                }
                if(incomingByte==53){
                  gas_value=analogRead(MQ7);
                  Serial.println(gas_value);
                }                
                if(incomingByte==54){
                  gas_value=analogRead(MQ8);
                  Serial.println(gas_value);
                }
                if(incomingByte==55){//calidad del aire (mq135)
                  gas_value=analogRead(MQ135);
                  Serial.println(gas_value);
                }
               if((err = dht11.read(hum, temp)) == 0)    // Si devuelve 0 es que ha leido bien
          { 
               if(incomingByte==56){//temperatura
                  Serial.println(temp);
                }
                if(incomingByte==57){//humedad
                  Serial.println(hum);
                }
          }
        }
    
   }


