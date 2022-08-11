from Prato import Prato

class Pizza(Prato):
    def __init__(self, nome, preco, data_val, peso, molho, recheio, borda):
        super().__init__(nome, preco, data_val, peso)
        self.__molho = molho
        self.__recheio = recheio
        self.__borda = borda

    @property
    def molho(self):
        return self.__molho

    @molho.setter
    def molho(self, molho):
        self.__molho = molho

    @property
    def recheio(self):
        return self.__recheio

    @recheio.setter
    def recheio(self, recheio):
        self.__recheio = recheio

    @property
    def borda(self):
        return self.__borda

    @borda.setter
    def borda(self, borda):
        self.__borda = borda
