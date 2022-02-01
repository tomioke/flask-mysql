from app import app
from app.controller import GuruController, SiswaController, UserController

@app.route('/')
def index():
    return 'Hello World!!'

@app.route('/guru', methods=['GET'])
def guru_s():
    return GuruController.index()

@app.route('/siswa', methods=['GET'])
def siswa_s():
    return SiswaController.index()

@app.route('/user', methods=['GET'])
def user_s():
    return UserController.index()