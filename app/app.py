from flask import Flask, render_template
from models.users import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rhema_life.db'

db.init_app(app)

# Import Blueprints
from routes.auth import login_bp as login_bp

# Register Blueprints
app.register_blueprint(login_bp, url_prefix='/auth')

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

