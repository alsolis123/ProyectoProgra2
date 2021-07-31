import random
import Entes

entes = Entes.Entes()


class matriz:

    def __init__(self):
        self.entes = 200
        self.lista = []
        self.listaCopia = []
        self.listaNumeros = []
        self.contadorVivos = 0
        self.contadorMuertos = 0
        self.contadorEnfermos = 0
        self.contadorSanos = 0

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
        
    def logica_Siguiente(self):
        self.listaCopia = self.lista.copy()
        
        for i in range(25):
            for j in range(25):
                
                if self.listaCopia[i][j] != 0:
                    x = i - 1
                    y = j - 1
                    if x >= 0 and y >= 0 and x <= 24 and y <= 24:
                        self.listaNumeros.append(self.listaCopia[x][y])
                    x = i - 1
                    y = j
                    if x >= 0 and y >= 0 and x <= 24 and y <= 24:
                        self.listaNumeros.append(self.listaCopia[x][y])
                    x = i - 1
                    y = j + 1
                    if x >= 0 and y >= 0 and x <= 24 and y <= 24:
                        self.listaNumeros.append(self.listaCopia[x][y])
                    x = i
                    y = j - 1
                    if x >= 0 and y >= 0 and x <= 24 and y <= 24:
                        self.listaNumeros.append(self.listaCopia[x][y])
                    x = i
                    y = j + 1
                    if x >= 0 and y >= 0 and x <= 24 and y <= 24:
                        self.listaNumeros.append(self.listaCopia[x][y])
                    x = i + 1
                    y = j - 1
                    if x >= 0 and y >= 0 and x <= 24 and y <= 24:
                        self.listaNumeros.append(self.listaCopia[x][y])
                    x = i + 1
                    y = j
                    if x >= 0 and y >= 0 and x <= 24 and y <= 24:
                        self.listaNumeros.append(self.listaCopia[x][y])
                    x = i + 1
                    y = j + 1
                    if x >= 0 and y >= 0 and x <= 24 and y <= 24:
                        self.listaNumeros.append(self.listaCopia[x][y])
                        
                    self.contadorVariable()
                    self.cambioVivosMuertos(i, j)
                    self.cambioSanosEnfermos(i, j)
                
                
                
        self.imprimirMatriz() #esto se tiene que eliminar
        
       
    
    def contadorVariable(self):
        self.contadorVivos = 0
        self.contadorMuertos = 0
        self.contadorEnfermos = 0
        self.contadorSanos = 0
        for n in self.listaNumeros:
            if n == 1 or n == 2 or n == 7 or n == 8:
                self.contadorVivos += 1
            elif n == 3 or n == 4 or n == 5 or n == 6:
                self.contadorMuertos += 1
            if n == 1 or n == 2 or n == 3 or n == 4:
                self.contadorSanos += 1
            elif n == 5 or n == 6 or n == 7 or n == 8:
                self.contadorEnfermos += 1  
        self.listaNumeros.clear()
    
    def cambioVivosMuertos(self, i, j):
        if self.contadorVivos >= 3:
                    pass
        elif self.contadorMuertos >= 4:
            if self.listaCopia[i][j] == 1:
                self.lista[i][j] = 3
            elif self.listaCopia[i][j] == 2:
                self.lista[i][j] = 4
            elif self.listaCopia[i][j] == 7:
                self.lista[i][j] = 5
            elif self.listaCopia[i][j] == 8:
                self.lista[i][j] = 6
                        
        
    def cambioSanosEnfermos(self, i, j):
        if self.contadorSanos >= 6:
            if self.lista[i][j] == 7:
                self.lista[i][j] = 1
            elif self.lista[i][j] == 8:
                self.lista[i][j] = 2
            elif self.lista[i][j] == 5:
                self.lista[i][j] = 3
            elif self.lista[i][j] == 6:
                self.lista[i][j] = 4
                
        elif self.contadorEnfermos >= 4:
            if self.lista[i][j] == 1:
                self.lista[i][j] = 7
            elif self.lista[i][j] == 2:
                self.lista[i][j] = 8
            elif self.lista[i][j] == 3:
                self.lista[i][j] = 5
            elif self.lista[i][j] == 4:
                self.lista[i][j] = 6
    #-----------------------------------------------------------------------------
    

