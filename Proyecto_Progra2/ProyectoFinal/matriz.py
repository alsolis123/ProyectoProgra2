import random
import Entes

entes = Entes.Entes()


class matriz:

    def __init__(self):
        self.entes = 200
        self.lista = []
    

    # Para crear la matriz inicial
    def crearMatriz(self):
        for i in range(25):
            self.lista.append([])
            for j in range(25):
                self.lista[i].append(0)
        self.rellenarEntes()        
        
    #Esto va a rellenar la matriz con los entes aleatorios
    def rellenarEntes(self):                
        while self.entes != 0:
            for i in range(25):
                for j in range(25):
                    ingresar = random.randint(1,6)
                    if ingresar == 2:
                        if self.lista[i][j] == 0:
                            if self.entes != 0:
                                tipo_ente = random.randint(1,8)
                                self.lista[i][j] = tipo_ente
                                self.entes -= 1
                            
    # Esto es para imprimir la matriz, mas adelante se podria eliminar
    def imprimirMatriz(self):
        for i in range(25):
            for j in range(25):
                print(self.lista[i][j], end=' ')
            print()
        
    # Esto es un contador que se utilizo unicamente como prueba para 
    #confirmar que se estan llenado los entes, hay que eliminarlo ya que no es necesario
    def contador(self):
        prueba = 0    
        for i in range(25):
            for j in range(25):
                if self.lista[i][j] != 0:
                    prueba += 1
        print(prueba)
    #-----------------------------------------------------------------------------
    #Ejecutando el codigo como prueba:

