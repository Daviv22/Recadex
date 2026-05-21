from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)
lista = []

@app.route('/', methods=['GET', 'POST'])
def recado():
    if request.method == 'POST':
        autor = request.form.get('autor')
        mensagem = request.form.get('mensagem')
        lista.append({"Autor": autor, "Mensagem": mensagem})
        print(lista)
        return redirect(url_for("recado"))
    
    # Se for GET (o usuário acabou de acessar), mostra o formulário
    return render_template('index.html', recado=lista)

@app.route("/recados", methods=['GET'])
def listar():
    return render_template('recados.html', lista=lista)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)