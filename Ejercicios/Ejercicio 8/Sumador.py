# -*- coding: utf-8 -*-
"""
Created on Sat Mar  8 02:30:27 2025

@author: Alex
"""

class Sumador:
    def __init__(self):
        self.total = 0

    def agregar_numero(self, numero):
        if numero != 0:
            self.total += numero
        return self.total  
