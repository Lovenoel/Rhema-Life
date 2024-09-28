from flask import Blueprint, url_for, redirect
from flask_login import current_user

login_bp = Blueprint('auth', __name__, url_prefix='/auth')

@login_bp.route('/register')
def register():
    return "I am a registerd user"

@login_bp.route('/login')
def login():
    """Endpoint for user login"""
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    else:
        return "I am so blessed"