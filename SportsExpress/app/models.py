from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Shoe:
    def to_dict(self):
        return {
            'id': self.id,
            'model': self.model,
            'gender': self.gender,
            'size': self.size
        }


class Shoes(db.Model,Shoe):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    size = db.Column(db.Integer, nullable=False)