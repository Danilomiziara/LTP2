class Veiculo:
    def __init__(self, valor, modelo, km=0):
        self.valor = valor
        self.modelo = modelo
        self.km = km
    def get_valor(self):
        return self.valor
    def get_modelo(self):
        return self.modelo
    def get_km(self):
        return self.km
    def set_valor(self, novo_valor):
        self.valor = novo_valor
    def set_modelo(self, novo_modelo):
        self.modelo = novo_modelo
    def set_km(self, novo_km):
        self.km = novo_km
    def __str__(self):
        v = f"Modelo: {self.modelo}, R$ {self.valor}, Km {self.km}"
        return v
    def atuliza_valor(self, aumento_valor):
        self.valor = self.valor + aumento_valor

        

class Carro(Veiculo):
    def __init__(self, valor, modelo, km= 0, portas=4):
        super().__init__(valor, modelo, km)
        self.portas = portas
    def get_portas(self):
        return self.portas
    def set_portas(self, novo_portas):
        self.portas = novo_portas
    def __str__(self):
        c = f"Modelo: {self.modelo}, R$ {self.valor}, Km {self.km}, quantidade de portas {self.portas}"
        return c

class Moto(Veiculo):
    def __init__(self, valor, modelo, km= 0, cilindrada= 0):
        super().__init__(valor, modelo, km)
        self.cilindrada = cilindrada
    def get_cilidrada(self):
        return self.cilindrada
    def set_cilindrada(self, nova_cilindrada):
        self.cilindrada = nova_cilindrada
    def __str__(self):
        m = f"Modelo: {self.modelo}, R$ {self.valor}, Km {self.km}, cilindrada {self.cilindrada}"
        return m