# Postwork sesión 3 -- Creación de paquetes y módulos
 
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


def pagos_distintos(tarjeta, *args):
    """
    Función que calcula un pago recurrente sobre la tarjeta con distintos montos mes a mes 
    """
    tarjeta['cargos'] = 0
    for arg in args:
        tarjeta['pagos'] = arg
        if tarjeta['deuda'] < tarjeta['pagos']:
            tarjeta['pagos'] = tarjeta['deuda']
            generar_reporte(tarjeta)
        tarjeta['deuda'] = tarjeta['nueva_deuda']





       


