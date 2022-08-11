from Prato import Prato

class Lanche(Prato):
    def __init__(self, nome, preco, data_val, peso, pao, molho, recheio):
        super().__init__(nome, preco, data_val, peso)
        self.__pao = pao
        self.__molho = molho
        self.__recheio = recheio

    @property
    def pao(self):
        return self.__pao

    @pao.setter
    def pao(self, pao):
        self.__pao = pao

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