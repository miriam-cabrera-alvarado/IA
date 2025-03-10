# Validador.py
class Validador:
    def __init__(self):
        pass

    def validar_numero(self, numero):
        if numero < 10:  # El número debe ser menor que 10
            return True  # Número válido
        return False  # Número no válido
