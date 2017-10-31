import webbrowser

# INICIO Alexander Daniel WebBrowser
print("Introduce la URL a navegar o introduce 0 para navegar por defecto: ")
url = input()
if(url == '0'):
    url = "https://esviernes.com/"

# Asignamos el navegador por defecto con get() y si no lo encuentra lanza una excepcion
try:
    navegador = webbrowser.get('windows-default')
except webbrowser.Error:
    print ("No se ha encontrado navegador.")

# Comando para abrir la URL en una nueva ventana
navegador.open_new(url)

# Comando para abrir la URL en una nueva tab
navegador.open_new_tab(url)

