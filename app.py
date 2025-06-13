from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.utils import secure_filename
import os
from tinydb import TinyDB

app = Flask(__name__)
# Secret key fixa em produção (pega do ambiente se existir)
app.secret_key = os.getenv('SECRET_KEY', 'minha-super-chave-secreta')

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Usuários fixos para login simples
USUARIOS = {
    "designer": "minhasenha123",
}

# Banco TinyDB
db = TinyDB('projetos.json')

# Função correta e compatível com sua versão
def carregar_projetos():
    return [dict(doc, doc_id=doc.doc_id) for doc in db]

def salvar_projetos(projetos):
    db.truncate()  # limpa tudo antes
    for projeto in projetos:
        db.insert(projeto)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in USUARIOS and USUARIOS[username] == password:
            session['logged_in'] = True
            session['username'] = username
            flash('Login bem-sucedido!', 'success')
            return redirect(url_for('portfolio'))
        else:
            flash('Usuário ou senha inválidos. Tente novamente.', 'error')

    return render_template('login.html')

@app.route('/portfolio', methods=['GET', 'POST'])
def portfolio():
    if not session.get('logged_in'):
        flash('Você precisa fazer login para acessar o portfólio.', 'info')
        return redirect(url_for('login'))

    projetos = carregar_projetos()

    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        link = request.form.get('link')
        image = request.files['image']

        if image and allowed_file(image.filename):
            filename = secure_filename(image.filename)
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            image.save(path)
            image_url = url_for('static', filename=f'uploads/{filename}')

            projetos.append({
                'title': title,
                'description': description,
                'image_url': image_url,
                'link': link
            })

            salvar_projetos(projetos)
            flash('Projeto adicionado com sucesso!', 'success')
        else:
            flash('Erro ao enviar a imagem. Verifique o formato (png, jpg, jpeg, gif).', 'error')

    return render_template('portfolio.html', username=session.get('username'), projetos=projetos)

@app.route('/logout')
def logout():
    session.clear()
    flash('Você foi desconectado.', 'info')
    return redirect(url_for('login'))

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/excluir/<int:id>')
def excluir_projeto(id):
    db.remove(doc_ids=[id])
    flash('Projeto excluído com sucesso!', 'success')
    return redirect(url_for('portfolio'))

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_projeto(id):
    if id == 0:
        # Novo projeto (vazio)
        projeto = {}
    else:
        projeto = db.get(doc_id=id)

        if not projeto:
            flash('Projeto não encontrado.', 'error')
            return redirect(url_for('portfolio'))

    if request.method == 'POST':
        # Se for novo, adiciona
        if id == 0:
            novo_projeto = {
                'title': request.form['title'],
                'description': request.form['description'],
                'link': request.form['link']
            }

            image = request.files['image']
            if image and allowed_file(image.filename):
                filename = secure_filename(image.filename)
                path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                image.save(path)
                novo_projeto['image_url'] = url_for('static', filename=f'uploads/{filename}')

            db.insert(novo_projeto)
            flash('Novo projeto adicionado com sucesso!', 'success')
        else:
            # Atualização de projeto existente
            projeto['title'] = request.form['title']
            projeto['description'] = request.form['description']
            projeto['link'] = request.form['link']

            image = request.files['image']
            if image and allowed_file(image.filename):
                filename = secure_filename(image.filename)
                path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                image.save(path)
                projeto['image_url'] = url_for('static', filename=f'uploads/{filename}')

            db.update(projeto, doc_ids=[id])
            flash('Projeto atualizado com sucesso!', 'success')

        return redirect(url_for('portfolio'))

    return render_template('editar.html', projeto=projeto, id=id, username=session.get('username'))

# Roda o app (produção não usa debug)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
