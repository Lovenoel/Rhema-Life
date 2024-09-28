from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

login_manager = LoginManager()
db = SQLAlchemy()


class User(db.Model):
    """Class representation of the User object"""
    'tablename' == 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email= db.Column(db.String(25), nullable=False, unique=True)

    def repr__(self):
        return f'<User {self.username}, {self.email}>'
    
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

    '''def __repr__(self) -> str:
        return super().__repr__()
    '''