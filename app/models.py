from app import db

class User(db.Model):

    # fields are created as instances of the db.Column which takes the field type
    # and other optional arguments
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)

    def __repr__(self):
        return '<User %r>' % (self.nickname)