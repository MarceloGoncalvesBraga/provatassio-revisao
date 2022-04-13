

from flask import Flask, redirect,render_template, url_for
from restaurante import Restaurante
from endereco import Endereco
app = Flask(__name__)
enderecos = [
    Endereco(1, 1, "Rj 127","1000", "Bnh", "Paracambi"),
    Endereco(2, 2, "Tupiniquim","127", "Centro", "vassouras"),
    Endereco(3, 3, "Ipiranga 127","403", "centro", "valenca"),
    Endereco(4, 4, "Senador amaral","12", "Novo Arco", "Sao Fideliz"),
    Endereco(5, 5, "Rj 093","23500", "Bnh", "Mendes")
]

lista = [
     Restaurante(1,"Toca da Traira","01.jpg","11:00 as 15:30","Luiz Gustavo","Torne o Almoco especial"),
     Restaurante(2,"Restaurante Caipirao","02.jpg","11:00 as 15:30","Luiz Gustavo","Comer Pode ser melhor"),
     Restaurante(3,"Restaurante da Rute","03.jpg","11:00 as 15:30","Luiz Gustavo","Delicias do Paladar"),
     Restaurante(4,"Alto da Serra Restaurante","04.jpg","11:00 as 15:30","Luiz Gustavo","Servir bem Hoje"),
     Restaurante(5,"Silva Restaurante","05.jpg","11:00 as 15:30","Andre Ricardo","Comer Hoje o Melhor"),

]




@app.route("/")
@app.route("/home")
def home():
    template_name = 'home.html'
    return render_template(template_name,
        restaurantes=lista
    )

@app.route("/restaurante/<int:id>")
def restaurante(id):
    for restaurante in lista:
        if restaurante.get_id() == id:
            for e in enderecos:
               if e.get_restaurante_id() == id:
                  endereco = e
            return render_template("exibir.html",
                enderecos = endereco,
                restaurante=restaurante,
                )
            
    return render_template("home.html", restaurantes=lista)





if __name__ == '__main__':
    app.run(debug=True) 