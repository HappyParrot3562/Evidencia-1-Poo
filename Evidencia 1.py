class Producto:
    objetos = []

    def __init__(self, name, tp, pricet, id, inv):
        pricet = float(pricet)
        tp = str(tp)
        Producto.objetos.append(self)
        if not (pricet > 0):
            raise ValueError("El precio debe ser positivo")
        match tp:
            case "Comida":
                self.priceP = pricet * 1.1
            case "Bebida":
                self.priceP = pricet * 1.1
            case "Medicina":
                self.priceP = pricet * 1.5
            case "Otro":
                self.priceP = pricet * 1.3
            case _:
                raise ValueError("El tipo tiene que ser comida, bebida, medicina o ser especificado como otro")
        self.nombre = name
        self.inventario = inv
        self.id = id
        self.pt = pricet
        self.tipo = tp


Galletas = Producto("Galletas", "Comida", 23.0, "A123", 20)
chips = Producto("Papas fritas", "Comida", 26.0, "P567Q", 25)
Refresco = Producto("Refresco", "Bebida", 13.0, "B456", 30)
WMineral = Producto("Agua Mineral", "Bebida", 15.0, "B789X", 15)
Aspirina = Producto("Aspirina", "Medicina", 30.0, "C789", 20)
Paracetamol = Producto("Paracetamol", "Medicina", 30.0, "M456Y", 35)
Rastrillo = Producto("Rastrillo", "Otro", 60.0, "D012", 15)
papel = Producto("Papel higiénico", "Otro", 30.0, "O123Z", 25)

Database = {"Galletas": Galletas, "Papas fritas": chips, "Refresco": Refresco, "Agua Mineral": WMineral,
            "Aspirina": Aspirina, "Paracetamol": Paracetamol, "Rastrillo": Rastrillo, "Papel higiénico": papel}

print("Bienvenido al OXXO")
print("Recuerda escribir correctamente el nombre del articulo o su ID exacto\n")
shopcar = 0
shoplist = []
t = 0


while True:
    encontrado = False
    choose = input("Ingrese el nombre o ID del producto: ")
    if choose == "F":
        lenght = len(shoplist)
        e = 1
        i = 0
        print("\nRecibo:")
        print("Productos Totales:", t)
        while i < lenght:
            print(e, shoplist[i]["Nombre"], shoplist[i]["Precio"])
            i += 1
            e += 1
        print("\nTotal a pagar:", shopcar)
        break
    else:
        for objetos in Database.values():
            if choose == objetos.nombre or choose == objetos.nombre.lower() or choose == objetos.id:
                if objetos.inventario == 0:
                    print("NO HAY STOCK\n")
                else:
                    print(objetos.nombre, objetos.priceP, "\n")
                    objetos.inventario -= 1
                    shopcar += objetos.priceP
                    t += 1
                    shoplist.append({"Nombre": objetos.nombre, "Precio": objetos.priceP})
                encontrado = True
        if not encontrado:
            print("No se encontró el producto")

print("¡¡Gracias por su compra!!")
