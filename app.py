from flask import Flask, request, url_for

from config import Config
from models import db
from notes.routers import notes_bp
from auth.routes import auth_bp

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
app.register_blueprint(notes_bp)
app.register_blueprint(auth_bp)

with app.app_context():
    db.create_all()

@app.route("/acerca-de")
def about():
    return "Esto es una app de notas."


@app.route("/contacto", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        return "formulario enviado correctamente", 201
    return "Pagina de contacto"


