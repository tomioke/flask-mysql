from app import app
from app.controller import GuruController, SiswaController, UserController
from flask import request

@app.route('/')
def index():
    return '<p>Selamat datang<p>'

@app.route('/guru', methods=['GET', 'POST'])
def guru_s():
    if request.method == 'GET':
        return GuruController.index()

    else:
        return GuruController.save()

@app.route('/guru/<id>', methods=['GET'])
def guruDetail(id):
    return GuruController.detail(id)

@app.route('/siswa', methods=['GET'])
def siswa_s():
    return SiswaController.index()

@app.route('/user', methods=['GET'])
def user_s():
    return UserController.index()