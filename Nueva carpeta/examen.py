from abc import ABC, abstractmethod
class Empleado(ABC):
    def __init__(self, rfc, apellidos, nombres):
        self._rfc = rfc
        self._apellidos = apellidos
        self._nombres = nombres
    def mostrar_info(self):
        return f"RFC {self._rfc}, Apellido {self._apellidos}, Nombre {self._nombres}"
    @abstractmethod
    def ingresos(self):
        pass
class EmpleadoVendedor(Empleado):
    def __init__(self, rfc, apellidos, nombres, monto_vendido, tasa_comision):
        super().__init__(rfc, apellidos, nombres)
        self.monto_vendido = monto_vendido
        self.tasa_comision = tasa_comision
    def ingresos(self):
        return self.calcular_ingresos()
    def calcular_ingresos(self):
        return self.monto_vendido * self.tasa_comision
    def calcular_bonificacion(self):
        ingresos = self.calcular_ingresos()
        if self.monto_vendido < 1000:
            return 0
        elif 1000 <= self.monto_vendido <= 5000:
            return 0.05 * ingresos
        else:
            return 0.10 * ingresos
    def calcular_descuento(self):
        ingresos = self.calcular_ingresos()
        if ingresos < 1000:
            return 0.11 * ingresos
        else:
            return 0.15 * ingresos
    def calcular_sueldo_neto(self):
        ingresos = self.calcular_ingresos()
        bonificacion = self.calcular_bonificacion()
        descuento = self.calcular_descuento()
        return ingresos + bonificacion - descuento
class EmpleadoPermanente(Empleado):
    def __init__(self, rfc, apellidos, nombres, sueldo_base, numero_seguro_social):
        super().__init__(rfc, apellidos, nombres)
        self.sueldo_base = sueldo_base
        self.numero_seguro_social = numero_seguro_social
    def ingresos(self):
        return self.sueldo_base
    def calcular_descuento(self):
        return 0.11 * self.sueldo_base
    def calcular_sueldo_neto(self):
        ingresos = self.ingresos()
        descuento = self.calcular_descuento()
        return ingresos - descuento
vendedor = EmpleadoVendedor("dsfgfdhg", "Gil", "Jorge", 2000, 0.1)
print(vendedor.mostrar_info())
print(f"Ingresos: {vendedor.ingresos()}")
print(f"Bonificación: {vendedor.calcular_bonificacion()}")
print(f"Descuento: {vendedor.calcular_descuento()}")
print(f"Sueldo Neto: {vendedor.calcular_sueldo_neto()}")
try:
    permanente = EmpleadoPermanente("dfhgfdh", "Aln", "Osornio", 1000, "3215433")
    print(permanente.mostrar_info())
    print(f"Ingresos: {permanente.ingresos()}")
    print(f"Descuento: {permanente.calcular_descuento()}")
    print(f"Sueldo Neto: {permanente.calcular_sueldo_neto()}")
except ValueError as e:
    print(e)
