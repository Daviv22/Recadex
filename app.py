from flask import Flask, request, render_template, redirect, url_for, flash

app = Flask(__name__)
# Necessário para usar mensagens 'flash' (sessões)
app.secret_key = 'uma_chave'

lista = []


@app.route('/', methods=['GET', 'POST'])
def recado():
    if request.method == 'POST':
        autor = request.form.get('autor')
        mensagem = request.form.get('mensagem')

        # Guardando em snake_case (padrão)
        lista.append({"autor": autor, "mensagem": mensagem})

        # Fornece um feedback para o usuário na próxima página
        flash("Recado enviado com sucesso!")
        return redirect(url_for("listar"))  # Redireciona direto para o mural

    return render_template('index.html')


@app.route("/recados", methods=['GET'])
def listar():
    return render_template('recados.html', lista=lista)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)