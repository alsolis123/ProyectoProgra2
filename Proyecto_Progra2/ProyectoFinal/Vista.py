from tkinter import *
import tkinter as Tk
import tkinter as ttk
import matriz

matr = matriz.matriz()

#hola
class Interfaz: 
    def __init__(self):
        self.root = Tk.Tk()
        #self.view = View(self.root)

    def ejecutarInicioMatriz(self):
        matr.crearMatriz()
        matr.imprimirMatriz()
    
    def NumerosaLetras(self, numero):
        salida = ""
        if numero == 1:
            salida = "HvS"
        elif numero == 2:
            salida = "MvS"
        elif numero == 3:
            salida = "HmS"
        elif numero == 4:
            salida = "MmS"
        elif numero == 5:
            salida = "HmE"
        elif numero == 6:
            salida = "MmE"
        elif numero == 7:
            salida = "HvE"
        elif numero == 8:
            salida = "MvE"
        else:
            salida = "-"
        return salida
    
    
        
    def menu(self):
        #comentario de prueba
        
        self.root.title("JUEGO DE LA VIDA")
        self.root.geometry("702x432")
        ##Pantalla de menú principal
        self.img1 = PhotoImage(file="ProyectoFinal\Imagenes\Juegodelavida.1.png")
        self.img = Label(self.root,image=self.img1).place(x=0,y=0)
        ##Botones del menu
        self.img1btn1= PhotoImage(file="ProyectoFinal\Imagenes\jugar.png")
        self.img1btn2= PhotoImage(file="ProyectoFinal\Imagenes\Salir.png")
        self.img1btn3= PhotoImage(file="ProyectoFinal\Imagenes\AjustesBG.png")
        self.boton = Button(self.root,image=self.img1btn1,height=41, width=177,borderwidth=0,command=self.juego).place(x=260,y=215)#Boton jugar
        self.boton = Button(self.root,image=self.img1btn2,height=41, width=177,borderwidth=0,command=self.root.destroy).place(x=260,y=265)#Boton salir
        self.boton = Button(self.root,image=self.img1btn3,height=43, width=44,borderwidth=0,command=self.ajuste).place(x=0,y=15)#Boton ajustes
        self.root.resizable(0,0)
        self.root.quit()
        self.root.deiconify()
        
        self.root.mainloop()

    def ajuste(self):
        ##Menu
        
        
        self.ajustes = Tk.Toplevel(self.root)
        self.ajustes.title("AJUSTES")
        self.ajustes.geometry("500x471")
        self.img2 = PhotoImage(file="ProyectoFinal\Imagenes\Ajustes.png")
        self.fnd2 = Label(self.ajustes,image=self.img2).place(x=0,y=0)
        self.ajustes.resizable(0,0)
        #Boton X
        
        
        self.Brillo = Scale(self.ajustes,from_=0,to=100, orient=HORIZONTAL,length=250).place(x=200,y=130)
        self.volumen = Scale(self.ajustes,from_=0,to=100, orient=HORIZONTAL,length=250).place(x=200,y=220)
        


    def juego(self):
        ##Juego
        self.root.withdraw()
        self.juegos = Tk.Toplevel(self.root)
        self.ejecutarInicioMatriz()
        self.juegos.title("JUEGO")
        self.juegos.geometry("1300x475")
        self.img3 = PhotoImage(file="ProyectoFinal\Imagenes\Juego.png")
        self.fnd3 = Label(self.juegos,image=self.img3).place(x=0,y=0)
        #
        
        for r in range(25):
            for c in range(25):
                cell = Entry(self.juegos, width=5)
                cell.grid(row=r, column=c)
                cell.insert(0, '{}'.format(self.NumerosaLetras(matr.lista[r][c])))
                
        self.juegos.resizable(0,0)
   
        ##BOTONES
        self.img3btn1= PhotoImage(file="ProyectoFinal\Imagenes\AjustesBG.png")
        self.img3btn2= PhotoImage(file="ProyectoFinal\Imagenes\Aniquilar.png")
        self.img3btn3= PhotoImage(file="ProyectoFinal\Imagenes\Enfermar.png")
        self.img3btn4= PhotoImage(file="ProyectoFinal\Imagenes\Siguiente.png")
        
        boton = Button(self.juegos,image=self.img3btn1,height=43, width=44,borderwidth=0,command=self.ajuste).place(x=550,y=10)#Boton Ajustes
        boton = Button(self.juegos,image=self.img3btn2,height=45, width=177,borderwidth=0).place(x=800,y=100)#Boton Aniquilar  
        boton = Button(self.juegos,image=self.img3btn3,height=45, width=177,borderwidth=0).place(x=800,y=200)#Boton Enfermar   
        boton = Button(self.juegos,image=self.img3btn4,height=45, width=177,borderwidth=0).place(x=800,y=300)#Boton Siguiente 

a=Interfaz()
a.menu()