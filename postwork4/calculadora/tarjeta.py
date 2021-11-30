class Tarjeta_credito:

    def __init__(self, nombre = None, tasa = 0, deuda = 0, pagos = 0, cargos = 0):
        self.__nombre = nombre
        self.__tasa = tasa
        self.__deuda = deuda
        self.__pagos = pagos
        self.__cargos = cargos

    def get_nombre(self):
        return self.__nombre


    def crea_tarjeta(self):
        """Función para ingresar nuevas tarjetas"""

        capturado = False
        while capturado == False:
        
            self.__nombre = input("Nombre del dueño de la tarjeta: ")
            self.__tasa = float( input( "Ingrese la tasa de interes anual de la tarjeta (%): "))
            self.__deuda = float( input( "Ingrese el monto de la deuda actual de la tarjeta: "))
            self.__pagos = float( input( "Ingrese el monto del pago que va a realizar: "))


            if self.__pagos > self.__deuda:
                print()
                print("No es posible realizar un pago mayor a la deuda!")
                print("Vuelve a ingresar la información")
            else:
                capturado = True
                self.__cargos = float( input( "Escribe el monto total de los nuevos cargos: "))
            


    def __captura_nueva_deuda(self):
        """ Función para calcular la nueva de la tarjeta despues de que se realiza un pago"""

        tasa_porcentaje = self.__tasa/100
        interes_mensual = tasa_porcentaje/12
        self.__deuda_recalculada = (self.__deuda - self.__pagos)*(1+interes_mensual)
        self.__nueva_deuda = self.__deuda_recalculada + self.__cargos
        



    def generar_reporte(self):
        """ Función para generar el reporte con la deuda de la tarjeta"""

        self.__captura_nueva_deuda()

        print()
        print("Resumen de tarjeta: ")
        print(55*"-")
        print("Tarjeta a nombre de:                       {}".format (self.__nombre))
        print("Tasa de interés anual:                     {}%".format (self.__tasa))
        print(55*"-")
        print("Deuda actual:                              {}".format (self.__deuda)) 
        print("Monto del pago:                            {}".format (self.__pagos))           
        print(55*"-")
        print("Deuda después del corte con intereses:     {}".format(self.__deuda_recalculada)) 
        print(55*"-")  
        print("Nuevos cargos del mes:                     {}".format (self.__cargos))    
        print(55*"-")
        print("Nueva deuda del mes:                       {}".format (self.__nueva_deuda)) 
        print(55*"-") 



    def pago_recurrente(self, monto):
        """Imprime el reporte de cada mes, para una serie de pagos del mismo monto en una tarjeta, 
            para una deuda que no tendrá nuevos cargos. Hasta convertir el valor de la deuda en 0"""

        self.__pagos = monto
        self.__cargos = 0
        while self.__deuda > 0:
            if self.__deuda < self.__pagos:
                self.__pagos = self.__deuda
            self.generar_reporte()
            self.__deuda = self.__nueva_deuda

    def pagos_distintos(self, *args):
        """ Función que calcula un pago recurrente sobre la tarjeta con distintos montos mes a mes """

        self.__cargos = 0
        for arg in args:
            self.__pagos = arg
            if self.__deuda < self.__pagos:
                self.__pagos = self.__deuda
            self.generar_reporte()
            self.__deuda = self.__nueva_deuda