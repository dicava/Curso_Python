# postwork Sesión 1 - Administrador de tarjetas de crédito

nom_duenio= input("Nombre del dueño de la tarjeta: ")
tasa_interes = float( input( "Ingrese la tasa de interes anual de la tarjeta (%): "))
tasa_porcentaje = tasa_interes/100
deuda_anterior = float( input( "Ingrese el monto de la deuda actual de la tarjeta: "))
pago_realizar = float( input( "Ingrese el monto del pago que va a realizar: "))


if pago_realizar > deuda_anterior:
    print()
    print("No es posible realizar un pago mayor a la deuda!")

else:
    cargos = float( input( "Escribe el monto total de los nuevos cargos: "))
    interes_mensual = tasa_porcentaje / 12
    deuda_desp_pago = deuda_anterior - pago_realizar
    deuda_recalculada = round( ( (deuda_anterior - pago_realizar) * (1 + interes_mensual) ) ,4 )
    nueva_deuda = deuda_recalculada + cargos

    print()
    print("Resumen de tarjeta: ")
    print(40*"-")
    print("Tarjeta a nombre de: {}".format (nom_duenio) )
    print("Tasa de interés anual: {}%".format (tasa_interes) )
    print(40*"-")
    print("Deuda actual: {}".format (deuda_anterior)) 
    print("Monto del pago: {}".format (pago_realizar))           
    print(40*"-")
    print("Deuda después de pago: ", round( (deuda_anterior - pago_realizar), 4) ) 
    print("Intereses del mes: ", round( (deuda_desp_pago*interes_mensual), 4) )    
    print(40*"-")
    print("Deuda recalculada: {} ".format (deuda_recalculada))       
    print("Nuevos cargos del mes: {} ".format (cargos))    
    print(40*"-")
    print("Nueva deuda del mes: {}".format (nueva_deuda))  