from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('Home.html')


@app.route('/cadastro')
def cadastro():
    return render_template('Cadastro.html')


@app.route('/login')
def login():
    return render_template('Login.html')


@app.route('/playlist')
def playlist():
    return render_template('Playlist.html')


@app.route('/player')
def player():
    return render_template('Player.html')


@app.route('/novamusica')
def nova_musica():
    return render_template('NovaMusica.html')


@app.route('/criarplaylist')
def criar_playlist():
    return render_template('CriarPlaylist.html')


@app.route('/editarplaylist')
def editar_playlist():
    return render_template('EditarPlaylist.html')


@app.route('/dentro')
def dentro():
    return render_template('Dentro.html')


if __name__ == '__main__':
    app.run(debug=True)
