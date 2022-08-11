from Prato import Prato

class Salgadinho(Prato):
    def __init__(self, nome, preco, data_val, peso, tipo, recheio, massa):
        super().__init__(nome, preco, data_val, peso)
        self.__tipo = tipo
        self.__recheio = recheio
        self.__massa = massa

    @property
    def recheio(self):
        return self.__recheio

    @recheio.setter
    def recheio(self, recheio):
        self.__recheio = recheio

    @property
    def massa(self):
        return self.__massa

    @massa.setter
    def massa(self, massa):
        self.__massa = massa

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo
