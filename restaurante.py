class Restaurante:
    def __init__(self, id, nome, img,horario, chefe ,comentario):
        self.__id = id
        self.__nome = nome
        self.__img = img
        self.__horario = horario
        self.__chefe = chefe
        self.__comentario = comentario
        
    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_img(self):
        return self.__img

    
    def get_horario(self):
            return self.__horario

    def get_chefe(self):
        return self.__chefe

    def get_comentario(self):
        return self.__comentario