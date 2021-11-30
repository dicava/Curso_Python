# Postwork sesión 3 -- Creación de paquetes y módulos

from calculadora.tarjeta import crea_tarjeta, pago_recurrente, pagos_distintos
from calculadora.usuario import multiples_reportes

tarjeta1 = crea_tarjeta()
tarjetas = [tarjeta1,tarjeta1,tarjeta1]
multiples_reportes(tarjetas)

pago_recurrente(tarjeta1, 2000)


tarjeta1 = {'nombre': 'Visa', 'tasa': 28.0, 'deuda': 10000, 'pagos': 3000, 'cargos': 1000}
tarjeta2 = {'nombre': 'MasterCard', 'tasa': 30.0, 'deuda': 23000, 'pagos': 4500, 'cargos': 1000}
print(tarjeta1)
multiples_reportes([tarjeta1,tarjeta2])


tarjeta3 = {'nombre': 'AMEX', 'tasa': 32.0, 'deuda': 70000, 'pagos': 5000, 'cargos': 1000}
pago_recurrente(tarjeta3, 5000)

pagos_distintos(tarjeta2, 1000, 2000, 1500)

