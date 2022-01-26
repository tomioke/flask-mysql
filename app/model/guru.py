from app import db

class Guru(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    nip = db.Column(db.String(30), nullable=False)
    nama = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(13), nullable=False)
    alamat = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return '<Guru {}>'.format(self.name)
