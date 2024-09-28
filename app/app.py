from flask import Flask, render_template
from models.users import db

app = Flask(__name__)
db.init_app(app)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

