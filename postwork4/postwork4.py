from calculadora.tarjeta import Tarjeta_credito
from calculadora.usuario import usuario

tarjeta1 = Tarjeta_credito(nombre='Visa', tasa=30, deuda=55000, pagos=1500)
tarjeta1.generar_reporte()

tarjeta2 = Tarjeta_credito(nombre='MasterCard', tasa=28, deuda=67000, pagos=1400)
tarjeta2.generar_reporte()


usuario1 = usuario(nombre='Roberto', tarjetas=[tarjeta1])
usuario1.agrega_tarjeta(tarjeta2)
usuario1.multiples_reportes()
usuario1.cancela_tarjeta('Visa')

usuario1.multiples_reportes()