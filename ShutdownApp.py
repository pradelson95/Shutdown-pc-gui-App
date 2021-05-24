from tkinter import *
from tkinter import messagebox
import os

ventana = Tk()
ventana.geometry("500x430")
ventana.config(bg="greenyellow")
ventana.title("My app")

messagebox.showwarning("Advertencia", "Si usted hace un click a los botones de la app, su pc se apagara o reiniciara en 10 segundos")

lblMessage = Label(ventana,bg="yellow", text="Hay dos botones abajo, uno para apagar su pc y otro para reiniciarlo", fg="red",font=("Arial",11))
lblMessage.place(x=2,y=50, width=495,height=30)

BtnShutdown = Button(ventana,font="Helveita,20", bg="violet", text="Shutdown",command= lambda:os.system("shutdown /s /t 10"))
BtnShutdown.place(x=10,y=130,width=150,height=100)

BtnRestart =  Button(ventana,font="Helveita,20",bg="lightblue", text="Restart", command=lambda:os.system("shutdown /r /t 10"))
BtnRestart.place(x=180,y=130, width=150,height=100)

ventana.mainloop()