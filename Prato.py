class Prato:
    def __init__(self, nome, preco, data_val, peso):
        self.__nome = nome
        self.__preco = preco
        self.__data_val = data_val
        self.__peso = peso

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, preco):
        self.__preco = preco

    @property
    def data_val(self):
        return self.__data_val

    @data_val.setter
    def data_val(self, data_val):
        self.__data_val = data_val

    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self, peso):
        self.__peso = peso

