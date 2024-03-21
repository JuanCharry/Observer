class Observer:
    def update(self, message):
        pass

class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)



class Usuario(Observer):
    def update(self, message):
        print("Usuario: Se ha realizado una compra.")

class Payment(Subject):
    def realizar_compra(self):
        print("Payment: Compra realizada.")
        self.notify("Compra realizada")

class CarritoDeCompras(Observer):
    def update(self, message):
        if message == "Compra realizada":
            print("CarritoDeCompras: Eliminando productos del carrito.")

class Inventario(Observer):
    def update(self, message):
        if message == "Compra realizada":
            print("Inventario: Descontando unidades de inventario.")


usuario = Usuario()
payment = Payment()
carrito_de_compras = CarritoDeCompras()
inventario = Inventario()

payment.attach(usuario)
payment.attach(carrito_de_compras)
payment.attach(inventario)

payment.realizar_compra()