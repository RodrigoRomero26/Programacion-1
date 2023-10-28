class Cuenta():
    def __init__(self, account= "", amount=0.0):
        self._account = account
        self._amount = amount
    @property
    def account (self):
        return self._account
    @account.setter
    def account (self, account):
        self._account = account
    
    @property
    def amount (self):
        return self._amount
    
    def mostrar(self):
        print(f"Propietario: {self._account}. Monto: {self._amount}")
    
    def ingresar(self,cant):
        if cant>0:
            self._amount += cant
    
    def retirar(self, cant):
        self._amount -= cant

