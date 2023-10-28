class Persona():
    def __init__(self, name="", age="", dni=""):
        self._name = name
        self._age = age
        self._dni = dni
    
    @property
    def name (self):
        return self._name
    @property
    def age (self):
        return self._age
    @property
    def dni (self):
        return self._dni
    
    @name.setter
    def name (self, name):
        if str(name).replace(" ", "").isalpha():
            self._name = name
        else:
            print("No ingresaste un nombre valido! Solo se aceptan letras.")
    
    @age.setter
    def age (self, age):
        if str(age).isdigit():
            self._age = age
        else:
            print("No ingresaste una edad valida! Solo se aceptan numeros.")
    
    @dni.setter
    def dni (self, dni):
        if (len(dni) == 7) or (len(dni)==8) and str(dni).isdigit():
            self._dni = dni
        else:
            print("No ingresaste un DNI valido! Solo se aceptan numeros de 7 u 8 digitos.")
    
    def mostrar(self):
        print(f"Nombre: {self.name}. Edad: {self.age}. DNI: {self.dni}")
    
    def esMayorDeEdad(self):
        if (int(self.age) >= 18):
            return True
        else:
            return False
