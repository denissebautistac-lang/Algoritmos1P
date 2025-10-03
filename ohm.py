#este progrma calcula la ley de ohm
print(" ley de ohm")
print("selecciona la opcion")
opcion=int(input("1=voltaje, 2=corriente, 3=resistencia:"))
try:
        if opcion==1:
            print("calcular voltaje")
            corriente=float(input("ingrese la corriente en amperios:"))
            resistencia=float(input("ingrese la resistencia en ohmios:"))
            voltaje=corriente*resistencia
            print("el voltaje es:",voltaje,"voltios")
        elif opcion==2:
            print("calcular corriente")
            voltaje=float(input("ingrese el voltaje en voltios:"))
            resistencia=float(input("ingrese la resistencia en ohmios:"))
            corriente=voltaje/resistencia
            print("la corriente es:",corriente,"amperios")
        elif opcion==3:
            print("calcular resistencia")
            voltaje=float(input("ingrese el voltaje en voltios:"))
            corriente=float(input("ingrese la corriente en amperios:"))
            resistencia=voltaje/corriente
            print("la resistencia es:",resistencia,"ohmios")
        else:
            print("opcion no valida")
except valueError:
        print("error: entrada no valida, por favor ingrese un numero"