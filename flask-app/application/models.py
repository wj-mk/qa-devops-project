from application import db

class Exoplanet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    system = db.Column(db.String(32))
    method = db.Column(db.String(32))
    year = db.Column(db.Integer())


