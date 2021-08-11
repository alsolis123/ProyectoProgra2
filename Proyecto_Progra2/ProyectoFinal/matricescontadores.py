class matricescontadores:
    
    def __init__(self):
        self.lista_reproducir = []
        self.lista_muertos = []
        self.lista_vida = []
        
    # Aca se inicializan todas las matrices con el valor 0, todas ellas son contadores
    def crearMatrizReproducir(self):
        for i in range(25):
            self.lista_reproducir.append([])
            self.lista_muertos.append([])
            self.lista_vida.append([])
            for j in range(25):
                self.lista_reproducir[i].append(0)
                self.lista_muertos[i].append(0)
                self.lista_vida[i].append(0)
    
    # Esta matriz es contador porque va a comenzar a contabilizar en caso que existan otros alrededor HoM
    def contarReproduccion(self, x, y, condicion):
        if condicion == True:
            if self.lista_reproducir[x][y] == 3:
                self.lista_reproducir[x][y] = 1
            else:
                self.lista_reproducir[x][y] += 1
        elif condicion == False:
            self.lista_reproducir[x][y] = 0
            
    #Esto contador siempre va a comenzar en 0 y va a revisar
    #cuantas veces un ente ha estado al lado de otro
    def contadorAleatorios(self):
        contador = 0
        for i in range(25):
            for j in range(25):
                if self.lista_reproducir[i][j] == 3:
                    contador += 1
        return contador
    
    #Va a contar cuanto llevan de estar muertos los entes
    def contarMuertos(self, x, y):
        if self.lista_muertos[x][y] == 2:
            self.lista_muertos[x][y] = 0
            return True
        elif self.lista_muertos[x][y] < 3:
            self.lista_muertos[x][y] +=1
            return False
        
    #Cuentan cuantos turnos llevan los entes, al octavo desaparecen
    def contadorViejos(self, x, y):
        if self.lista_vida[x][y] == 7:
            self.lista_vida[x][y] = 0
            return True
        elif self.lista_vida[x][y] < 8:
            self.lista_vida[x][y] += 1
            return False