#Clase Item
class Item:
    def __init__ (self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
                
    def calcular_subtotal(self):
        return f"self.precio * self.cantidad"

    def __str__(self):
        return f"{self.nombre} | Precio: ${self.precio:.2f} | Cantidad: {self.cantidad} | Subtotal: ${self.calcular_subtotal():.2f}"


class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return f"{self.nombre} - $ {self.precio}"



class Pedido:
    def __init__(self):
        self.items = []

#Agregar un nuevo item
    def agregar_item(self, nombre, precio, cantidad):
        nuevo_item = Item(nombre, precio, cantidad)
        self.items.append(nuevo_item)
        print(f"Ítem '{nombre_producto} x {precio} x {cantidad}' agregado al pedido.")

#Mostrar listado producto
    def mostrar_items(self):
        if not self.items:
            print(" El pedido está vacío.")
        else:
            print("\n Lista de ítems en el pedido:")
            for item in self.items:
                print(item)
                
# calcular sub total   
    def calcular_total(self):
        return sum(item.calcular_subtotal() for item in self.items)

#Mostrar detalle
    def mostrar_detalle(self):
        print("\n DETALLE DEL PEDIDO")
        if not self.items:
            print("El pedido está vacío.")
            return

        for item in self.items:
            print(item)

        print(f"\nTOTAL A PAGAR: $ {self.calcular_total()}")