# -*- coding: utf-8 -*-
"""
Created on Sat Mar  8 00:23:48 2025

@author: Alex
"""

class Validador:
    def __init__(self):
        self.contador = 0  

    def registrar_numero(self, numero):
        """Cada vez que se ingresa un número válido, incrementa el contador."""
        self.contador += 1  
        return self.contador  
