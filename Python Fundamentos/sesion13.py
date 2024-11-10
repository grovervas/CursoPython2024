class Cuenta:
    
    def __init__(self, archivo):
        self.archivo = archivo
        with open(archivo, 'r') as file:
            self.saldo = int(file.read())
    
    def depositar(self, monto):
        self.saldo = self.saldo + monto
        self.commit()
    
    def retirar(self, monto):
        self.saldo = self.saldo - monto
        self.commit()
    
    def commit(self):
        with open(self.archivo, 'w') as file:
            file.write(str(self.saldo))
    

cuenta = Cuenta("balance.txt")
print("Saldo:", cuenta.saldo)
cuenta.retirar(600)
print("Saldo:", cuenta.saldo)
cuenta.depositar(1000)
print("Saldo:", cuenta.saldo)
