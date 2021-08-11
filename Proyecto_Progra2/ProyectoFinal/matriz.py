
import random
import matricescontadores

mcontadores = matricescontadores.matricescontadores()

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
        self.contadorsexo = 0
        self.condicionNacimiento = True
        self.contadorNacimientos = 0

    #Esto basicamente va a ir a consultar si hay nuevos nacimientos, 
    #Si por 5 turnos no hay nacimiento entonces arrojara un booleano a la principal 
    #para detener la ejecucion
    def condicionSiContinua(self):
        condicion = False
        if self.condicionNacimiento == True:
            self.contadorNacimientos += 1
        elif self.condicionNacimiento == False:
            self.contadorNacimientos = 0
            
        self.condicionNacimiento = False
        if self.contadorNacimientos == 5:
            condicion = False
        else:
            condicion = True
        return condicion
        


    # Para crear la matriz inicial
    def crearMatriz(self):
        for i in range(25):
            self.lista.append([])
            for j in range(25):
                self.lista[i].append(0)
        self.rellenarEntes()        
        mcontadores.crearMatrizReproducir()
        
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
    def contadorEntes(self):
        contador = 0
        for i in range(25):
            for j in range(25):
                if self.lista[i][j] != 0:
                    contador += 1
        print(contador)
        return contador
        
    def logica_Siguiente(self):
        self.listaCopia = self.lista.copy()
        
        for i in range(25):
            for j in range(25):
                #Esta es toda la rama de consulta para saber que tienen alrededor
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
                        
                    self.contadorVariable(i, j)
                    self.cambioVivosMuertos(i, j)
                    self.cambioSanosEnfermos(i, j)
                    self.condicionEliminarMuertos(i, j)
                    self.eliminarEntesViejos(i, j)
                    mcontadores.contarReproduccion(i, j, self.contadorSexoContrario())
        self.agregarNuevosEntes()
                
    #Este es como el de eliminar entes viejos, va a eliminar cuando se cumpla la condicion del contador
    #Este consulta las matrices contadores    
    def condicionEliminarMuertos(self, x, y):
        if self.listaCopia[x][y] == 3 or self.listaCopia[x][y] == 4 or self.listaCopia[x][y] == 5 or self.listaCopia[x][y] == 6:
            condicion = mcontadores.contarMuertos(x, y)
            if condicion == True:
                self.lista[x][y] = 0
    
    #Este va a eliminar los entes viejos a menos que cambien
    #Si cambia a uno vivo por alguna razon entonces el valor del contador
    #pasara a ser 0            
    def eliminarEntesViejos(self, x, y):
        if self.lista[x][y] != 0:
            condicion = mcontadores.contadorViejos(x, y)
            if condicion == True:
                self.lista[x][y] = 0
                
    #Estos son los contadores individuales de uno en uno
    def contadorVariable(self, x, y):
        self.contadorVivos = 0
        self.contadorMuertos = 0
        self.contadorEnfermos = 0
        self.contadorSanos = 0
        self.contadorsexo = 0
        for n in self.listaNumeros:
            if n == 1 or n == 2 or n == 7 or n == 8:
                self.contadorVivos += 1
            elif n == 3 or n == 4 or n == 5 or n == 6:
                self.contadorMuertos += 1
            if n == 1 or n == 2 or n == 3 or n == 4:
                self.contadorSanos += 1
            elif n == 5 or n == 6 or n == 7 or n == 8:
                self.contadorEnfermos += 1
            if self.listaCopia[x][y] == 1 or self.listaCopia[x][y] == 3 or self.listaCopia[x][y] == 5 or self.listaCopia[x][y] == 7:
                if n == 2 or n == 4 or n == 6 or n == 8:
                    self.contadorsexo += 1
            if self.listaCopia[x][y] == 2 or self.listaCopia[x][y] == 4 or self.listaCopia[x][y] == 6 or self.listaCopia[x][y] == 8:
                if n == 1 or n == 3 or n == 5 or n == 7:
                    self.contadorsexo += 1
                    
        self.listaNumeros.clear()
    
    #Este metodo y el de abajo van a efectuar los cambios en la matriz principal
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
                        
    #Este metodo y el de arriba van a efectuar los cambios en la matriz principal    
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
                
                
    #Esta es la condicion que pasa como parametro arriba para el contador de reproduccion
    def contadorSexoContrario(self):
        if self.contadorsexo >= 1:
            self.condicionNacimiento = True
            return True
        else:
            
            return False
        
    #Aqui es donde principalmente se van a insertar los entes aleatorios    
    def insertarEnteAleatorio(self):
        condicion = False
        ente = random.randint(1,8)
        contador = 0
        if self.contadorEntes() > 400 and self.contadorEntes() < 625:
            for x in range(25):
                for y in range(25):
                    if self.lista[x][y] == 0 and contador <= 0:
                        contador += 1
                        self.lista[x][y] = ente
        #Una vez que se llega a 400 la formula le cuesta encontrar lugares 
        # y sobre carga el codigo por es despues de eso va a ir agregando en orden                
        elif self.contadorEntes() <= 400:
            condicion = False
            while condicion == False:
                aleatorioX = random.randint(0, 24)
                aleatorioY = random.randint(0, 24)
                if self.lista[aleatorioX][aleatorioY] == 0:
                    condicion = True
                    self.lista[aleatorioX][aleatorioY] = ente
                    
    #Esto va a ir a la matriz que verifica si se pueden agregar nuevos entes
    #o sea que hay hombre y mujer juntos y va a agregar todos aquellos entes nuevos    
    def agregarNuevosEntes(self):
        contador = mcontadores.contadorAleatorios()
        for x in range (contador):
            self.insertarEnteAleatorio()
            
    # Logica para enfermar un Ente de manera aleatoria
    def enfermarEnte(self):
        condicion = False
        #Esta condicion se rompera cuando encuentre un ente para enfermar
        while condicion == False:
            aleatorioX = random.randint(0, 24)
            aleatorioY = random.randint(0, 24)
            if self.lista[aleatorioX][aleatorioY] != 0:
                if self.lista[aleatorioX][aleatorioY] == 1:
                    condicion = True
                    self.lista[aleatorioX][aleatorioY] = 7
                elif self.lista[aleatorioX][aleatorioY] == 2:
                    condicion = True
                    self.lista[aleatorioX][aleatorioY] = 8
                elif self.lista[aleatorioX][aleatorioY] == 3:
                    condicion = True
                    self.lista[aleatorioX][aleatorioY] = 5
                elif self.lista[aleatorioX][aleatorioY] == 4:
                    condicion = True
                    self.lista[aleatorioX][aleatorioY] = 6
                
        
    #-----------------------------------------------------------------------------
    

