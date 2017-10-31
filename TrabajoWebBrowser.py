# Importa el webbrowser para poder usar el navegador
# Importa el os para poder usar comandos de windows como el cls
import webbrowser, os

# INICIO Alexander Daniel WebBrowser
salida='1'
while(salida!='0'):
    opcion='0'
    # Lanza el comando "cls" a través del sistema
    os.system('cls')
    print("Introduce la URL a navegar o introduce 0 para navegar por defecto: ")
    url = input()
    if(url == '0'):
        url = "https://esviernes.com/"

    # Registra el navegador que queremos usar, al no usarlo coge el por defecto
    # Da un error close_fds que no es compatible con windows.
    ## webbrowser.register(name, constructor, instance=None)

    # Asignamos el navegador por defecto con get() y si no lo encuentra lanza una excepcion
    try:
        navegador = webbrowser.get('windows-default')
    # Excepción lanzada si no encuentra un navegador
    except webbrowser.Error:
        print("No se ha encontrado navegador.")

    while(opcion!='1' and opcion!='2'):
        # Muestra la url usando el navegador por defecto, si "new" es 0 la url se abre en la misma
        # ventana del navegador si es posible. Si es 1 abre un nuevo navegador, si es 2 abre un nuevo
        # "tab". Si "autorise" es True te trae al frente la ventana si es posible.
        ## webbrowser.open(url, new=0, autoraise=True)
        print("Abrir en una nueva pestaña o nueva ventana? 1-Ventana || 2-Pestaña")
        opcion = input()
        if(opcion == '1'):
            # Comando para abrir la URL en una nueva ventana
            navegador.open_new(url)
        elif(opcion == '2'):
            # Comando para abrir la URL en una nueva tab
            navegador.open_new_tab(url)
        else:
            print("Opcion incorrecta.")

    print("Quiere salir del programa o abrir otra web? 0-Salir || 1-Seguir")
    salida=input()
    if(salida == '0'):
        print("Salida del programa.")
    
