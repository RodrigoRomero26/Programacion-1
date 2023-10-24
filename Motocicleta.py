class Motocicleta():
    status = "new"
    engine = False
    def __init__(self, color="black", registration="asd123", fuel="10", wheels="2", brand="bmw", model="diablo", fabrication_date=2023, max_velocity=400, weight=300):
        self.color = color
        self.registration = registration
        self.combustible_litros = fuel
        self.numero_ruedas = wheels
        self.brand = brand
        self.model = model
        self.fabrication_date = fabrication_date
        self.maxvelocity = max_velocity
        self.weight = weight
    
    def start (self):
        if (self.engine == False):
            self.engine = True
            print("El motor se encendio")
        else:
            print("El motor ya esta encendido.")
    
    def stop (self):
        if (self.engine == True):
            self.engine = False
            print("El motor fue apagado")
        else:
            print("El motor ya esta apagado")
    
    def showprice(self):
        try:
            print(f"El precio de la motocicleta {self.brand} modelo {self.model} es {self.price}")
        except:
            print("La motocicleta no tiene precio")
