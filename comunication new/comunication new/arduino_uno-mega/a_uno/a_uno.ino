int led = 0;        // asigna a LED el valor 13
int boton =33 ;       // asigna a botón el valor 33
int valor = 0;       // define el valor y le asigna el
                     // valor 0

void setup()
{
pinMode(boton2, OUTPUT); // configura el led (pin13) como salida
pinMode(boton, INPUT); // configura botón (pin7) como entrada
}

void loop()
{

digitalWrite(led, HIGH);   // envía a la salida 'led' el valor leído
Serial.print(boton);
}

