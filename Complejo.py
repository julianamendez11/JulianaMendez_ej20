import numpy as np

class Complejo():
    def __init__(self,real,imaginario):
        self.imaginario=imaginario
        self.real=real
        
    def conjugado(self):
        return -self.imaginario
    
    def calcula_norma(self):
        return np.sqrt(self.imaginario**2 + self.real**2)
            
    def pow(self, n):
        return (self.real+self.imaginario)**n
        
