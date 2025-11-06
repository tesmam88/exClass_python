class Horario:
    def __init__(self, hora=0, minuto=0, segundo=0):
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo
        self.normalizar()  # garante que o horário comece válido

    def normalizar(self):
        """Ajusta o horário se os segundos ou minutos passarem de 59."""
        # Transforma tudo em segundos totais
        total_segundos = self.hora * 3600 + self.minuto * 60 + self.segundo
        
        # Ajusta para formato padrão (0–23 horas)
        total_segundos %= 24 * 3600
        
        self.hora = total_segundos // 3600
        self.minuto = (total_segundos % 3600) // 60
        self.segundo = total_segundos % 60

    def incrementar(self, segundos):
        """Incrementa o horário em uma certa quantidade de segundos."""
        self.segundo += segundos
        self.normalizar()

    def diferenca(self, outro_horario):
        """Calcula a diferença em segundos entre dois horários."""
        # Converte ambos para segundos totais
        total1 = self.hora * 3600 + self.minuto * 60 + self.segundo
        total2 = outro_horario.hora * 3600 + outro_horario.minuto * 60 + outro_horario.segundo
        
        return abs(total1 - total2)

    def __str__(self):
        """Retorna o horário formatado como HH:MM:SS."""
        return f"{self.hora:02d}:{self.minuto:02d}:{self.segundo:02d}"



h1 = Horario(10, 59, 50)
print("Horário inicial:", h1)

h1.incrementar(15)
print("Após incremento de 15s:", h1)

h2 = Horario(11, 0, 30)
print("Outro horário:", h2)

diferenca = h1.diferenca(h2)
print("Diferença em segundos:", diferenca)