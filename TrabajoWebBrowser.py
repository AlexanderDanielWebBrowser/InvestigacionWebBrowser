# Importamos webbrowser para poder usar los comandos de webbrowser
# Importamos os para poder usar los comandos del sistema
import webbrowser, os
from tkinter import *
from tkinter import messagebox

def navegar():
    opcion = v.get()

    if(e.get() == ''):
        e.insert(0, "www.esviernes.com")

    url = e.get()

    try:
        # webbrowser.get() permite seleccionar el navegador que usaremos, en este caso usamos el navegador por defecto
        navegador = webbrowser.get('windows-default')
    # Si el webbrowser.get() nos da error enseñamos un mensaje que nos avisa
    except webbrowser.Error:
        messagebox.showwarning("Error", "No se ha encontrado navegador.")

    if(opcion == 1):
        # navegador.open_new(url) abre una nueva ventana con la url que le pasamos
        navegador.open_new(url)
    elif(opcion == 2):
        # navegador.open_new_tab(url) abre una nueva pestaña en el navegador con la url que le pasamos
        navegador.open_new_tab(url)
    else:
        messagebox.showwarning("Error", "Selecciona una opcion")

titulo="Navegador"
icono = os.path.join(os.path.dirname(__file__), 'icon.ico')

root = Tk()
root.title(titulo)
root.iconbitmap(icono)
root.resizable(False, False)

l = Label(root, text="URL")
l.pack()

e = Entry(root, width=50, justify=CENTER)
e.pack()

v = IntVar()
Radiobutton(root, text="Nueva Ventana", variable=v, value=1).pack()
Radiobutton(root, text="Nueva Pestaña", variable=v, value=2).pack()

b = Button(root, text="Ir", command=navegar)
b.config(bd=3,relief=GROOVE)
b.pack(fill=BOTH, expand=1)

root.mainloop()
