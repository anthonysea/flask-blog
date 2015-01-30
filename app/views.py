from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'Lil B'}
	posts = [
		{
			'author': {'nickname': 'John'},
			'body': 'Faggot'
		},
		{
			'author': {'nickname': 'Smithe'},
			'body': 'Tom Cruise'
		}
	]
	return render_template('index.html',
						   title='Home',
						   user=user,
						   posts=posts)
