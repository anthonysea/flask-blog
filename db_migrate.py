import imp  # internals of the import command
from migrate.versioning import api
from app import db
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO

# gets the current version of the db under version control of the specified repo
v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)

migration = SQLALCHEMY_MIGRATE_REPO + ('/versions%03d_migration.py' % (v + 1))

# returns a new empty module called old_model
tmp_module = imp.new_module('old_model')

# dump the current db as a python model to stdout
old_model = api.create_model(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)

exec(old_model, tmp_module.__dict__)

# creates a script changing the old Python model to the new model
script = api.make_update_script_for_model(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, tmp_module.meta, db.metadata)

open(migration, "wt").write(script)

# upgrades the database to a later version
api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)

# shows the current version of DATABASE_URI under version control of the MIGRATE_REPO
v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)

print('New migration saved as ' + migration)
print('Current database version: ' + str(v))