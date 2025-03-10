# -*- coding: utf-8 -*-
"""
Created on Wed Mar  5 00:33:34 2025

@author: Alex
"""
from datetime import datetime

class Descuento:
    def __init__(self, fecha, monto):
        self.fecha = datetime.strptime(fecha, "%Y-%m-%d").date()
        self.monto = float(monto)

    def calcular_descuento(self):
        if self.fecha.month == 10:  # Octubre es el mes 10
            return self.monto * 0.85  # 15% de descuento
        return self.monto   