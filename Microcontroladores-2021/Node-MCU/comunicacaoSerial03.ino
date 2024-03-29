#define LED1 14
#define LED2 13
#define LED3 12
#define LED_LIGADO 0
#define LED_DESLIGADO 1
#define BOTAO1 5
#define BOTAO2 4
#define BOTAO_LIGADO 0
#define BOTAO_DESLIGADO 1

void inicializa_hardware() {
  //Configura as saídas
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
  pinMode(LED3, OUTPUT);
  //Garante que as saídas estão desligadas
  digitalWrite(LED1, LED_DESLIGADO);
  digitalWrite(LED2, LED_DESLIGADO);
  digitalWrite(LED3, LED_DESLIGADO);
  //Configurar as entradas
  pinMode(BOTAO1, INPUT_PULLUP);
  pinMode(BOTAO2, INPUT_PULLUP);

  //Inicializa a comunicação
  Serial.begin(9600); //9600,19200,38400(bluetooth),115200(ethernet)
}

int contadora = 100;
char msg[50];

void setup() {
  inicializa_hardware();
  Serial.println("Inicio da contagem");
}

void loop() {
  sprintf(msg, "Contagem: %d", contadora);
  Serial.println(msg);
  delay(1000);
  contadora++;
  if (contadora >= 10) {
    Serial.println("Plus Ultra");
    contadora = 0;
  }
}
