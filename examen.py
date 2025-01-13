class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre  # Atributo público: nombre del cliente
        self._numero_de_pedido = None  # Atributo privado: número de pedido
        self.comida_ordenada = None  # Atributo público: comida ordenada
    def realizar_pedido(self, comida):
        try:
            if not comida:
                raise ValueError("La comida no puede estar vacía.")
            self.comida_ordenada = comida
            print(f"Pedido realizado: {comida}")
        except ValueError as e:
            print(f"Error al realizar el pedido: {e}")

    def revisar_datos(self):
        try:
            if not self.nombre:
                raise ValueError("El nombre del cliente no está definido.")
            resultado = f"Nombre del cliente: {self.nombre}, Comida ordenada: {self.comida_ordenada}"
            print(resultado)
            return resultado
        except ValueError as e:
            resultado = f"Error: {e}"
            print(resultado)
            return resultado

# Clase heredada: Informes
class Informes(Cliente):
    def __init__(self, nombre, numero_de_cliente):
        super().__init__(nombre)
        self.numero_de_cliente = numero_de_cliente

    def emitir_comprobante(self):
        resultado = f"Comprobante: Cliente {self.nombre}, Número de Cliente: {self.numero_de_cliente}, Comida: {self.comida_ordenada}"
        print(resultado)
        return resultado

    def preparar_plato(self):
        if self.comida_ordenada:
            resultado = f"Preparando {self.comida_ordenada} para el cliente {self.nombre}."
        else:
            resultado = "No hay comida ordenada para preparar."
        print(resultado)
        return resultado

# Clase ControlDePedido
class ControlDePedido:
    def __init__(self, numero_de_pedido, comida_ordenada):
        self.numero_de_pedido = numero_de_pedido
        self.comida_ordenada = comida_ordenada

    def preparar_plato(self):
        resultado = f"Preparando el plato: {self.comida_ordenada}, Número de Pedido: {self.numero_de_pedido}."
        print(resultado)
        return resultado

# Clase Pedidos
class Pedidos:
    def __init__(self, numero_de_pedido, comida_ordenada):
        self.numero_de_pedido = numero_de_pedido
        self.comida_ordenada = comida_ordenada

    def generar_pedido(self):
        resultado = f"Pedido generado: Número {self.numero_de_pedido}, Comida: {self.comida_ordenada}."
        print(resultado)
        return resultado

# Clase Cocina
class Cocina:
    def __init__(self, numero_de_pedido, comida_ordenada, chef):
        self.numero_de_pedido = numero_de_pedido
        self.comida_ordenada = comida_ordenada
        self.chef = chef

    def emitir_plato(self):
        resultado = f"El chef {self.chef} ha preparado el plato: {self.comida_ordenada}, Número de Pedido: {self.numero_de_pedido}."
        print(resultado)
        return resultado

# Ejemplo de uso directo
def main():
    cliente = Cliente("Ana Gómez")
    cliente.realizar_pedido("Ensalada César")
    cliente.revisar_datos()

    informe = Informes("Ana Gómez", 12345)
    informe.emitir_comprobante()
    informe.preparar_plato()

    control = ControlDePedido(101, "Pizza Margherita")
    control.preparar_plato()

    pedido = Pedidos(202, "Sopa de tomate")
    pedido.generar_pedido()

    cocina = Cocina(303, "Lasagna", "Chef Luigi")
    cocina.emitir_plato()

# Ejecutar el ejemplo de uso
if __name__ == "__main__":
    main()
