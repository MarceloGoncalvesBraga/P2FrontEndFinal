
from application.model.entity.postagem import Postagem
#class Dao:
class PostagemDao:

    def lista_postagens():
        #Retorar uma lista de noticias!
        listar_postagens = [
         Postagem(id=1,titulo="Suécia está mais segura agora, diz chefe da Otan",id_usuario=1, texto="Stoltenberg afirma que nações ocidentais deram garantias de segurança ao país, l.",data_postagem="13/06/2022",likes=23),
         Postagem(id=2,titulo="em para o Brasil? Jornal espanhol informa que dois gigantes",id_usuario=1, texto="Luís Suárez é um dos principais nomes do futebol mundial que está disponível, de 35 anos, ns.",data_postagem="13/06/2022",likes=53),
         Postagem(id=3,titulo="Casagrande se revolta e faz desabafo sobre governo no Encontro",id_usuario=2, texto="A participação de Casagrande no Encontro desta segunda-feira (13) deu o que falara .",data_postagem="12/06/2022",likes=45),
         Postagem(id=4,titulo="Prova dificil sem um python executavel",id_usuario=2, texto="Uma prova acontecendo em tempo real mais o aluno nao tem sua ferramenta de linguagem instalada corretamente",data_postagem="01/02/2022",likes=23),
         Postagem(id=5,titulo="Uma grande ideia",id_usuario=3, texto="outra coisa acontecendo",data_postagem="13/06/2022",likes=23),


         ]

        return listar_postagens

