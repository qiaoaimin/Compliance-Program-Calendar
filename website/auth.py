from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)


@auth.route('/auth', methods=['GET', 'POST'])
def auth_manage():
    return render_template('auth_page.html')
