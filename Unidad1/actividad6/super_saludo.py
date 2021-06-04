from datetime import datetime #importamos el modulo datetime para traer la informacion del tiempo
now = datetime.now() #utilizamos la funcion now del modulo que nos retornara la hora actual del sistema

if(now.hour >= 3 and now.hour <= 11): #con now.hour traemos solamente el dato de hora y lo comparamos si esta en el rango de 3am a 11am
    print("Buenos Dias, son las", now.hour)#si es verdadero imprime el saludo de buenos días
elif(now.hour >= 12 and now.hour <= 18): #comparamos la hora entre las 12 del dia y las 6 de la tarde.
#hay que mencionar que el formato esta en horario militar.
    # si es verdadero imprime el saludo de buenas tardes
    print("Buenos Tardes, son las", now.hour)
else:# si no cumple con las dos primeras condiciones quiere decir que esta en el rango de 6pm a 2am
    print("Buenos Noches, son las", now.hour)
