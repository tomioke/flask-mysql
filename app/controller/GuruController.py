from app.model.guru import Guru
from app.model.siswa import Siswa
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

def detail(id):
    try:
        guru = Guru.query.filter_by(id=id).first()
        siswa = Siswa.query.filter(Siswa.id_guru == id)

        if not guru:
            return response.badRequest([], "Tidak ada data guru!")

        datasiswa = formatSiswa(siswa)
        data = singleDetailSiswa(guru, datasiswa)
        
        return response.success(data, "status success")
    except Exception as e:
        print(e)

def singleDetailSiswa(guru, siswa):
    data = {
        'id': guru.id,
        'nip': guru.nip,
        'nama': guru.nama,
        'phone': guru.phone,
        'alamat': guru.alamat,
        'siswa': siswa
    }

    return data

def singleSiswa(siswa):
    data = {
        'id': siswa.id,
        'no_urut': siswa.no_urut,
        'nama': siswa.nama,
        'phone': siswa.phone,
        'kelas': siswa.kelas,
        'alamat': siswa.alamat,
        'id_guru': siswa.id_guru
    }

    return data

def formatSiswa(data):
    array = []

    for i in data:
        array.append(singleSiswa(i))

    return array

# Menyimpan dan menambahkan data guru
def save():
    try:
        nip = request.form.get('nip')
        nama = request.form.get('nama')
        phone = request.form.get('phone')
        alamat = request.form.get('alamat')

        gurus = Guru(nip=nip, nama=nama, phone=phone, alamat=alamat)
        db.session.add(gurus)
        db.session.commit()

        return response.success(data, 'Sukses menambahkan data!') #
    except Exception as e:
        print(e)



