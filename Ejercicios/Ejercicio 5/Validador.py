# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 02:03:15 2025

@author: Alex
"""
class Validador:
    def __init__(self):
        pass

    def validar_numero(self, numero):
        if 0 <= numero <= 20:  
            return True  
        return False  
