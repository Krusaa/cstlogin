from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
	return render_template('index.html')

@main.route('/players.html')
def players():
    return render_template('players.html')

@main.route('/teams.html')
def teams():
    return render_template('teams.html')


@main.route('/profile')
@login_required
def profile():
	return render_template('profile.html', name=current_user.name)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')