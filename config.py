import os

WTF_CSRF_ENABLED = True
SECRET_KEY = 'lil b is goat'

basedir = os.path.abspath(os.path.dirname(__file__))

# path to the db
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
# folder where SQLAlchemy-migrate files will br stored
SQLALCHEMY_MIGRATE_REPO =  os.path.join(basedir, 'db_repository')
