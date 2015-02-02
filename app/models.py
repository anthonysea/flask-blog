from app import db


class User(db.Model):

    # fields are created as instances of the db.Column which takes the field type
    # and other optional arguments
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)

    # db.relationship - defined on the one side of the one-to-many relationship
    # gets the user.posts member that gets us a list of posts from the user
    # first argument to the db.relationship defines the "many" class of the relationship
    # backref - defines the field that will be added to the objects of the "many" class
    # this means that post.author can be used on the posts to retrieve the User instance that created
    # the post
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User %r>' % self.nickname


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % self.body