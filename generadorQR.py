import qrcode

# Pregunta que texto queremos codificar:
texto = input("Introduzca el mensaje a codificar: ")


# Clase con valores para generar la imagen:
qr = qrcode.QRCode(
    version=None, #especifica el tamaño. Con None es flexible.
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=20,
    border=4,
)

# Generamos la imagen con el texto indtroducido:
qr.add_data(texto)
qr.make(fit=True)

imagen = qr.make_image(fill_color="black", back_color="white")


# Guardamos la imagen generada, con el nombre de archivo que queramos:
nombre_archivo = input("Nombre de la imagen generada: ")
imagen.save(nombre_archivo)
