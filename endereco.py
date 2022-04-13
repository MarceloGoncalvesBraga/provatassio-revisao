class Endereco:
    def __init__(self, id, restaurante_id, rua,numero, bairro, cidade ):
        self.__id = id
        self.__restaurante_id = restaurante_id
        self.__rua = rua
        self.__numero= numero
        self.__bairro = bairro
        self.__cidade= cidade
        
    def get_id(self):
        return self.__id

    def get_restaurante_id(self):
        return self.__restaurante_id

    def get_rua(self):
        return self.__rua
    
    def get_numero(self):
        return self.__numero
    
    def get_bairro(self):
        return self.__bairro

    def get_cidade(self):
        return self.__cidade