import webbrowser, os
from tkinter import *
from tkinter import messagebox

def navegar():
    opcion = v.get()

    if(e.get() == ''):
        e.insert(0, "www.esviernes.com")

    url = e.get()

    try:
        navegador = webbrowser.get('windows-default')
    except webbrowser.Error:
        messagebox.showwarning("Error", "No se ha encontrado navegador.")

    if(opcion == 1):
        navegador.open_new(url)
    elif(opcion == 2):
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