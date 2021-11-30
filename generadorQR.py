import qrcode


# Generando la imagen del código QR con la información que queramos:

texto = input("Introduzca el mensaje a codificar: ")

imagen = qrcode.make(texto)



# Guardamos la imagen generada, con el nombre de archivo que queramos:
nombre_archivo = input("Nombre de la imagen generada: ")
imagen.save(nombre_archivo)