from application import main
from application.model.dao.postagem_dao import PostagemDao
from application.model.entity.postagem import Postagem
from application.model.dao.usuario_dao import UsuarioDao
from application.model.entity.usuario import Usuario
import datetime
from flask import Flask, render_template, request, jsonify

@main.route("/nova-postagem")
def nova_postagem():
    return render_template("nova-postagem.html",
    )

@main.route("/exibir_postagen/<int:id>")
def exibir_postagen(id):
    postagens = PostagemDao.lista_postagens()
    usuarios = UsuarioDao.lista_usuario()

    for postagen in postagens:

        if postagen.get_id() == id:
            for usuario in usuarios:
               if usuario.get_id() == postagen.get_id_usuario():
                  usuario1 = usuario.get_nome()

            return render_template("exibir-postagem.html",
                postagem=postagen,
                usuario = usuario1,  
                 )
    return render_template("home.html", postagens=PostagemDao.lista_postagens())

@main.route("/salvar", methods=['POST', 'GET'])
def Salvar():    
  postagens = PostagemDao.lista_postagens()
  if request.method == "POST":
    id_usuario = request.form.get('id_usuario', '...')

    if id_usuario != "": 
      some = 0
      id_usuario = request.form.get('id_usuario', 1)
      titulo = request.form.get('titulo', 'Sem titulo')
      texto = request.form.get('texto', '...')
      #data = datetime
      data_postagem = request.form.get('data_postagem', '13/06/2022')
      like = request.form.get('like', 1)
      if len(titulo) == "":
        print("Titulo vazio nao aceito")
        some = 1      
      elif len(texto) == "" or len(texto) >= 200 :
        print("Texto Muito Grande")
        some = 1    
      if some == 0:

       postagens.append((Postagem(id=100,titulo=titulo,id_usuario=id_usuario,texto=texto, data_postagem=data_postagem,likes=like)))
       #postagens = PostagemDao.lista_postagens()
       return render_template("index.html",
         postagens= postagens    
         )
      postagens = PostagemDao.lista_postagens()
      return render_template("index.html",
       postagens= postagens    
       )
  postagens = PostagemDao.lista_postagens()
  return render_template("index.html",
    postagens= postagens    
    )

@main.route("/likes/",methods=['POST'])
def Like():    
  postagens = PostagemDao.lista_postagens()
  json = request.get_json()
  postagem_id = json['postagem_id']
  for postagen in postagens:
      if postagen.get_id() == postagem_id:
       result = postagen.set_likes(1)
       result = 10
       return jsonify(total=result)
       #return print(total) 

@main.route('/like/conte/<int:id>', methods=['POST'])
def Curtir(id):
    json = request.get_json()
    postagem_id = json['postagem_id']
    postagens = PostagemDao.lista_postagens()
    for postagen in postagens:
      if postagen.get_id() == id:
       result = postagen.set_likes(1)
       print(result)
    return jsonify(total=result)
#--------------------------------------------------------
#  python nao tava rodando no novo pc entao nao testei
#----------------------------------------------------------
