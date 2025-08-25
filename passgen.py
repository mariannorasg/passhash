# Importo las librerías necesarias
import random # Para las funciones de aletoriedad
import string # Para tener los "paquetes" de caracteres
import os # Funciones del sistema operativo, crear carpetas, archivos, etc
from datetime import datetime # Para obtener la fecha y hora usados en el nombre del archivo para no pisar los antiguos

# Defino la longitud de la contraseña mediante un input numérico
longitud = int(input("Ingrese el tamaño de su contraseña: "))

# Defino que caracteres van a conformar la contraseña
caracteres = string.ascii_letters + string.digits + string.punctuation

# Defino la contraseña mediante un orden random de los caracteres que le pasé anteriormente
password = "".join(random.choice(caracteres) for i in range(longitud))

# Carpeta fija donde se van a guardar las contraseñas
carpeta = r"C:\Users\maikt\Desktop\Contraseñas"
os.makedirs(carpeta, exist_ok=True)  # Crea la carpeta si no existe

# Nombre del archivo con fecha/hora para que no se pisen
nombre_archivo = f"password-{datetime.now().strftime('%Y%m%d-%H%M%S')}.txt"
ruta = os.path.join(carpeta, nombre_archivo)

# Guarda la contraseña en el archivo
with open(ruta, "w", encoding="utf-8") as f:
    f.write(password)

# Muestra resultados, tanto contraseña como la ruta donde se guardó
print("La contraseña generada es: " + password)
print("Guardada en:" + ruta)
