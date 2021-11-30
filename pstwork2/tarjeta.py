# Postwork sesión 2
 
def crea_tarjeta():
    """Función para ingresar nuevas tarjetas"""

    capturado = False
    while capturado == False:
        
        nom_duenio= input("Nombre del dueño de la tarjeta: ")
        tasa_interes = float( input( "Ingrese la tasa de interes anual de la tarjeta (%): "))
        tasa_porcentaje = tasa_interes/100
        deuda_anterior = float( input( "Ingrese el monto de la deuda actual de la tarjeta: "))
        pago_realizar = float( input( "Ingrese el monto del pago que va a realizar: "))


        if pago_realizar > deuda_anterior:
            print()
            print("No es posible realizar un pago mayor a la deuda!")
            print("Vuelve a ingresar la información")
        else:
            capturado = True
            cargos = float( input( "Escribe el monto total de los nuevos cargos: "))
            tarjeta_data = {'nombre': nom_duenio, 'tasa':tasa_interes, 'deuda': deuda_anterior, 'pagos': pago_realizar, 'cargos': cargos}
        return tarjeta_data


def captura_nueva_deuda(tarjeta):
    """ Función para calcular la nueva de la tarjeta despues de que se realiza un pago"""

    tasa_decimal = tarjeta['tasa']/100
    interes_mensual = tasa_decimal/12
    tarjeta['deuda_recalculada'] = round(((tarjeta['deuda'] - tarjeta['pagos'])*(1+interes_mensual)),4)
    tarjeta['nueva_deuda'] = round((tarjeta['deuda_recalculada'] + tarjeta['cargos']),4)
    return tarjeta



def generar_reporte(tarjeta):
    """ Función para generar el reporte con la deuda de la tarjeta"""
    tarjeta = captura_nueva_deuda(tarjeta)
   
    print()
    print("Resumen de tarjeta: ")
    print(55*"-")
    print("Tarjeta a nombre de:                       {}".format (tarjeta['nombre']))
    print("Tasa de interés anual:                     {}%".format (tarjeta['tasa']))
    print(55*"-")
    print("Deuda actual:                              {}".format (tarjeta['deuda'])) 
    print("Monto del pago:                            {}".format (tarjeta['pagos']))           
    print(55*"-")
    print("Deuda después del corte con intereses:     {}".format(tarjeta['deuda_recalculada'])) 
    print(55*"-")  
    print("Nuevos cargos del mes:                     {}".format (tarjeta['cargos']))    
    print(55*"-")
    print("Nueva deuda del mes:                       {}".format (tarjeta['nueva_deuda'])) 
    print(55*"-") 



def multiples_reportes(tarjetas):
    """función que itere sobre una lista de tarjetas e imprima los reportes de todas"""
    for tarjeta in tarjetas:
        generar_reporte(tarjeta)



def pago_recurrente(tarjeta, monto):
    """Imprime el reporte de cada mes, para una serie de pagos del mismo monto en una tarjeta, 
    para una deuda que no tendrá nuevos cargos. Hasta convertir el valor de la deuda en 0"""

    tarjeta['pagos'] = monto
    tarjeta['cargos'] = 0
    while tarjeta['deuda'] > 0:
        if tarjeta['deuda'] < tarjeta['pagos']:
            tarjeta['pagos'] = tarjeta['deuda']
        generar_reporte(tarjeta)
        tarjeta['deuda'] = tarjeta['nueva_deuda']




tarjeta1 = {'nombre': 'Visa', 'tasa': 28.0, 'deuda': 10000, 'pagos': 3000, 'cargos': 1000}
tarjeta2 = {'nombre': 'MasterCard', 'tasa': 30.0, 'deuda': 23000, 'pagos': 4500, 'cargos': 1000}
print(tarjeta1)
multiples_reportes([tarjeta1,tarjeta2])


tarjeta3 = {'nombre': 'AMEX', 'tasa': 32.0, 'deuda': 70000, 'pagos': 5000, 'cargos': 1000}
pago_recurrente(tarjeta3, 5000)



       


