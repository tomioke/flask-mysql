from app import db
from app.model.guru import Guru

class Siswa(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    no_urut = db.Column(db.String(30), nullable=False)
    nama = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(13), nullable=False)
    kelas = db.Column(db.String(10), nullable=False)
    alamat = db.Column(db.Text, nullable=False)
    id_guru = db.Column(db.BigInteger, db.ForeignKey(Guru.id))

    def __repr__(self):
        return '<Siswa {}>'.format(self.name)