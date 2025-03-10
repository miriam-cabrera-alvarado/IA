# -*- coding: utf-8 -*-
"""
Created on Sat Mar  8 19:34:51 2025

@author: Alex
"""

# Sumador.py
class suma100:
    def __init__(self):
        self.total = 0  

    def agregar_numero(self, numero):
        
        self.total += numero  
        return self.total  

    def ha_superado_limite(self):
        
        return self.total > 100
