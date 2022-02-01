from app.model.guru import Guru

from app import response, app, db
from flask import request

def index():
    try:
        guru = Guru.query.all()
        data = formatarray(guru)
        return response.success(data, "success")

    except Exception as e:
        print(e)

def formatarray(datas):
    array=[]

    for i in datas:
        array.append(singleObject(i))

    return array

def singleObject(data):
    data = {
        'id': data.id,
        'nip': data.nip,
        'nama': data.nama,
        'phone': data.phone,
        'alamat': data.alamat

    }

    return data


