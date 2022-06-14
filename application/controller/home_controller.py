
from flask import Flask, render_template, url_for
from application.model.dao.postagem_dao import PostagemDao
from application.model.dao.usuario_dao import UsuarioDao
from application import main
from application.model.entity.postagem import Postagem
from application.model.entity.usuario import Usuario

@main.route("/")
def home():
    postagens = PostagemDao.lista_postagens()
    return render_template("index.html",
       postagens= postagens
    )

