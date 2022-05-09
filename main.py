import tkinter as tk
from filosofos_beta import *



class GUI():
    def __init__(self):
        self.window= tk.Tk()
        self.window.title("Que pasa")

        self.texto=tk.Text(self.window, height=30,width=80)
        self.scroll= tk.Scrollbar(self.window)

        self.veces_comidas=[]
        self.estado_filosofos= []
        self.estado_tenedores= []

        self.info()
        
        self.texto.configure(yscrollcommand= self.scroll.set)
        self.texto.pack(side= tk.LEFT)
        self.scroll.config(command= self.texto.yview)
        self.scroll.pack(side= tk.RIGHT,fill= tk.Y)

        

        

        
    def info(self):        
        for i in range(N):
          entry = tk.Entry(self.window)
          entry.place(x=450, y=50+i*20)
          self.veces_comidas.append(entry)

          filosofos= tk.Label(self.window, text= "Filósofo " + str(i) + ":",bg="white")
          filosofos.place(x=350, y=50+i*20)

          tenedores= tk.Label(self.window, text= "Tenedor " + str(i),bg="grey")
          tenedores.place(x=350, y=200+i*20)

          
          self.estado_filosofos.append(filosofos)
          self.estado_tenedores.append(tenedores)
          
        tk.Label(self.window, text= "¿Cuántas veces han comido?").place(x=450, y= 20)

        tk.Canvas(self.window, width= 200, height=110, bg="grey").place(x = 400, y = 350)

        tk.Label(self.window, text="Comiendo", bg="White").place(x =430, y = 353)
        tk.Label(self.window, text="Pensando", bg="White").place(x =430, y = 380)

        tk.Label(self.window, text="Tenedor cogido", bg="White").place(x =430, y = 410)
        tk.Label(self.window, text="Tenedor libre", bg="White").place(x =430, y = 440)

        tk.Canvas(self.window, width= 10, height=10, bg="yellow").place(x = 410, y = 355)
        tk.Canvas(self.window, width= 10, height=10, bg="white").place(x = 410, y = 385)
        tk.Canvas(self.window, width= 10, height=10, bg="green").place(x = 410, y = 415)
        tk.Canvas(self.window, width= 10, height=10, bg="grey").place(x = 410, y = 445)

              
    def logs(self,texto):
        self.texto.insert(tk.END, str(texto)+"\n")

    def run(self):
      self.window.mainloop()
      
if __name__=="__main__":
    ventana= GUI()
    
    lista=[]
    for i in range(N):
        lista.append(filosofo(ventana)) 

    for f in lista:
        f.start()   
    
    ventana.run()

    for f in lista:
        f.join() 

