print("Simulacion de cajero automatico")
#Se asume que el nombre de usuario y contraseña se entrego al usuario en plataforma dias atras
# El usuario es: CLIENTE01
# La clave es ABC123
intentosusuario=[]
intentosclave=[]
saldo=0
intentos=1

while intentos<=3:
    print("Bienvenido al sistema de cajero automatico")
    print("Intento de acceso", intentos)
    usuario=input("Ingrese su usuario ")
    clave=input("Ingrese su contraseña ")
    intentosusuario.append(usuario)
    intentosclave.append(clave)
    if usuario=="CLIENTE01" or usuario=="cliente01":
        if clave=="ABC123":
            intentos=0
            print("Datos correctos")
            print("")
            opcion=1
            while opcion>=1:
                print("Elija la opcion requerida:")
                print("1. Depositar dinero a la cuenta")
                print("2. Sacar dinero de la cuenta ")
                print("3. Ver saldo")
                print("4. Salir")
                opcion=input()
                if opcion.isdigit()==True:
                    opcion=float(opcion)
                    if opcion==1:
                        print("")
                        print("Deposito de dinero")
                        deposito=input("Digite la cantidad a depositar: ")
                        if deposito.isdigit()==True:
                            deposito=float(deposito)
                            saldo=saldo+deposito
                            print("Su nuevo saldo es de", saldo)
                            print("")

                        else:
                            print("XXX  ERROR  XXX")
                            print("Para el deposito digite solo numeros")
                            print("")
                                        

                    elif opcion==2:
                        print("")
                        print("Retiro de dinero")
                        print("Su saldo es de: ",saldo)
                        retiro=input("Ingrese la cantidad a retirar: ")
                        if retiro.isdigit()==True:
                            retiro=float(retiro)
                            if saldo<retiro:
                                print("XXX Fondos insuficientes XXX")
                            elif saldo>retiro:
                                if retiro % 1000==0:
                                    saldo=saldo-retiro    
                                    print("Su nuevo saldo es de", saldo)
                                    print("")
                                elif retiro % 1000 != 0:
                                    print("Solo se puede retirar en billetes de 1000")

                        else:
                            print("XXX  ERROR  XXX")
                            print("Para el retiro digite solo numeros")
                            print("")



                    elif opcion==3:
                        print("")
                        print("Ver saldo")
                        print("Su saldo es de: ", saldo)
                    
                    elif opcion>4:
                        print("Opcion incorrecta, intente de nuevo")
                        print("")
                        
                    elif opcion==4:
                        print("XXX  SALIR  XXX")
                        print("")
                        opcion=0

                else:
                        print("Error digite una opcion, no letras ")
                        opcion=1
                        


                    
        elif clave != "ABC123":
            print("XXX  Datos incorrectos  XXXX")
            print("")
    else:
        print("XXXX Datos de acceso incorrectos XXXX")
        print("")

   
    intentos=intentos+1 
else:
    print("")
    print("Supero la cantidad de intentos")
    print("XXXXX  Cuenta bloqueda   XXXXX")
    print("")

    
