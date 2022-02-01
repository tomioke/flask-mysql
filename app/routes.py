from app import app
from app.controller import GuruController

@app.route('/')
def index():
    return 'Hello World!!'

@app.route('/guru', methods=['GET'])
def gurus():
    return GuruController.index()