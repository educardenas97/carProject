int boton =52 ;       // asigna a botón el valor 33
int valor = 0;       // define el valor y le asigna el
int boton2 =50 ;                 // valor 0

void setup()
{

pinMode(boton, INPUT); // configura botón (pin7) como entrada
pinMode(boton2, OUTPUT); // configura botón (pin7) como entrada

  Serial.begin(9600);
}

void loop()
{
  digitalWrite(boton2, HIGH);   // envía a la salida 'led' el valor leído
  valor = digitalRead(boton); //lee el estado de la entrada botón

  Serial.print("hi");
delay(500);

}

