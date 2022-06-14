
from application.model.entity.usuario import Usuario
#class Dao:
class UsuarioDao:

    def lista_usuario():
        #Retorar uma lista de noticias!
        lista_usuarios = [
          Usuario(id=1,nome="marcelo",matricula="202110474"),
          Usuario(id=2,nome="joao",matricula="202110674"),
          Usuario(id=3,nome="Alfed",matricula="202112474"),

         ]

        return lista_usuarios

