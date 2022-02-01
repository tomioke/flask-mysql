from app.model.siswa import Siswa
from app import response, app, db
from flask import request

def index():
    try:
        siswa = Siswa.query.all()
        data = formatarray(siswa)
        return response.success(data, "success")
    except Exception as e:
        print(e)

def formatarray(datas):
    array = []

    for i in datas:
        array.append(singleObject(i))

    return array

def singleObject(data):
    data = {
        'id': data.id,
        'no_urut': data.no_urut,
        'nama': data.nama,
        'phone': data.phone,
        'kelas': data.kelas,
        'alamat': data.alamat,
        'id_guru': data.id_guru,
    }

    return data
