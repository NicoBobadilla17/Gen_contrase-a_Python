import string
import random
#variable para preguntar al usuario, de tipo entero
longitud = int(input("Ingrese el tamaño de la contraseña :  "))

#variable de caracteres
#metod .ascci_letters para mayusculas y minusculas
#metod .digits genero digitos
#metod . punctuation genero signos de puntuacion
caracteres = string.ascii_letters + string.digits + string.punctuation

#variable contraseña
#metod .join para concatenar caracteres
# .join(random.choice()) se encarga de concatenar los caracteres aleatoriamente de 
# los metodos de la variable caracteres
# se concatenaran los caracteres segun la variable longitud
contraseña = "".join(random.choice(caracteres) for i in range(longitud))

print("la contraseña generada es: " + contraseña)


