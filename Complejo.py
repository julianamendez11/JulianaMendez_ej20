import numpy as np

class Complejo():
    def __init__(self,real,imaginario):
        self.imaginario=imaginario
        self.real=real
        
    def conjugado(self):
        return -imaginario
    
    def calcula_norma(self):
        return np.sqrt(imaginario**2 + real**2)
            
    def pow(self,n):
        return (real+imaginario)**n
        
