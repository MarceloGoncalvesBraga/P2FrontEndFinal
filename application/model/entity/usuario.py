class Usuario:

    def __init__(self, id, nome,matricula):
        self.__id = id
        self.__nome = nome
        self.__matricula = matricula

        
    def get_id(self):
        return self.__id
    
    def get_nome(self):
        return self.__nome

    def get_matricula(self):
        return self.__matricula


