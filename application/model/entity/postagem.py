class Postagem:

    def __init__(self, id, titulo,id_usuario, texto, data_postagem, likes):
        self.__id = id
        self.__titulo = titulo
        self.__id_usuario = id_usuario
        self.__texto = texto
        self.__data_postagem = data_postagem
        self.likes = likes
        
    def get_id(self):
        return self.__id
    
    def get_titulo(self):
        return self.__titulo

    def get_id_usuario(self):
        return self.__id_usuario

    def get_texto(self):
        return self.__texto

    def get_data_postagem(self):
        return self.__data_postagem
    
    def get_likes(self):
        return self.likes

    def set_likes(self,like):
       total = self.likes + like
       return total
    

