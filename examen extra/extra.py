class Cliente:
    def __init__(self, id_cliente, nombre):
        # Encapsulación solo para id_cliente
        self.__id_cliente = id_cliente
        self.nombre = nombre

    def realizar_pedido(self):
        print(f"El cliente {self.nombre} está realizando un pedido.")

    def revisar_datos(self):
        return {
            "ID Cliente": self.__id_cliente,
            "Nombre": self.nombre
        }


class Informes:
    def __init__(self, numero_pedido, comida_ordenada, precio_comida):
        # Atributos públicos
        self.numero_pedido = numero_pedido
        self.comida_ordenada = comida_ordenada
        self.precio_comida = precio_comida

    def crear_pedido(self):
        print(f"Pedido {self.numero_pedido} creado: {self.comida_ordenada} por ${self.precio_comida}.")

    def emitir_comprobante(self):
        return {
            "Número de Pedido": self.numero_pedido,
            "Comida Ordenada": self.comida_ordenada,
            "Precio": self.precio_comida
        }

    def preparar_plato(self):
        print(f"Preparando el plato: {self.comida_ordenada}.")


class Pedidos(Informes):
    def __init__(self, numero_pedido, id_cliente, comida_ordenada, precio_comida):
        # Herencia: Inicialización de la clase padre
        super().__init__(numero_pedido, comida_ordenada, precio_comida)
        self.id_cliente = id_cliente

    def mostrar_detalles_pedido(self):
        return {
            "Número de Pedido": self.numero_pedido,
            "ID Cliente": self.id_cliente,
            "Comida Ordenada": self.comida_ordenada,
            "Precio": self.precio_comida
        }


class ControlDePedidos:
    def __init__(self, id_pedido, id_cliente, numero_pedidos, costo_pedidos):
        # Atributos públicos
        self.id_pedido = id_pedido
        self.id_cliente = id_cliente
        self.numero_pedidos = numero_pedidos
        self.costo_pedidos = costo_pedidos

    def preparar_plato(self, comida):
        print(f"El plato {comida} está siendo preparado.")

    def calcular_costo_total(self):
        try:
            # Manejo de errores en la suma de costos
            return sum(self.costo_pedidos)
        except TypeError:
            print("Error: Los costos deben ser números.")
            return 0


class Cocina:
    def __init__(self, platos_disponibles, cocinero):
        # Atributos públicos
        self.platos_disponibles = platos_disponibles
        self.cocinero = cocinero
        self.platos_preparados = []

    def emitir_plato(self, plato):
        if plato in self.platos_disponibles:
            self.platos_preparados.append(plato)
            self.platos_disponibles.remove(plato)
            print(f"El plato {plato} ha sido emitido por {self.cocinero}.")
        else:
            # Manejo de errores cuando el plato no está disponible
            print(f"Error: El plato {plato} no está disponible en este momento.")


# Ejemplo de uso
try:
    cliente1 = Cliente(1, "Juan Perez")
    cliente1.realizar_pedido()
    print(cliente1.revisar_datos())

    pedido1 = Pedidos(101, 1, "Pizza", 12.50)
    pedido1.crear_pedido()
    print(pedido1.mostrar_detalles_pedido())

    control = ControlDePedidos(101, 1, 1, [12.50])
    control.preparar_plato("Pizza")
    print(f"Costo total: ${control.calcular_costo_total()}")

    cocina = Cocina(["Pizza", "Pasta", "Ensalada"], "Chef Luigi")
    cocina.emitir_plato("Pizza")
except Exception as e:
    print(f"Se produjo un error inesperado: {e}")