from flask import redirect, request, render_template, url_for, Blueprint, flash, session
from models import Note, db


notes_bp = Blueprint("notes", __name__)

@notes_bp.route("/")
def home():
    if "user" not in session:
         flash("Para poder ver las notas debes iniciar sessión", "error")
         return redirect(url_for("auth.login"))
    notes = Note.query.all()
    return render_template("home.html", notes=notes)


@notes_bp.route("/crear-nota", methods=["GET", "POST"])
def create_note():
    if request.method == "POST":
        title = request.form.get("title", "")
        content = request.form.get("content", "")

        if not len(title.strip()) > 2:
            flash("El título es muy corto, minimo 2 caracteres", "error")
            return render_template("note_form.html")
        

        if  len(title.strip()) > 30:
            flash("El título es muy largo, máximo 30 caracteres", "error")
            return render_template("note_form.html")


        if not len(content.strip()) > 3:
            flash("El contenido es muy corto, minimo 3 caracteres", "error")
            return render_template("note_form.html")


        note_db = Note(title=title, content=content)
        db.session.add(note_db)
        db.session.commit()
        flash("Nota creada", "success")
        return redirect(url_for("notes.home"))
    return render_template("note_form.html")


@notes_bp.route("/editar-nota/<int:id>", methods=["GET", "POST"])
def edit_note(id):
    note = Note.query.get_or_404(id)
    if request.method == "POST":
        title = request.form.get("title", "")
        content = request.form.get("content", "")

        if not len(title.strip()) > 2:
            flash("El título es muy corto, minimo 2 caracteres", "error")
            return render_template("edit_note.html", note=note)
        

        if  len(title.strip()) > 30:
            flash("El título es muy largo, máximo 30 caracteres", "error")
            return render_template("edit_note.html", note=note)


        if not len(content.strip()) > 3:
            flash("El contenido es muy corto, minimo 3 caracteres", "error")
            return render_template("edit_note.html", note=note)


        note.title = title
        note.content = content
        db.session.commit()
        return redirect(url_for("notes.home"))

    return render_template("edit_note.html", note=note)


@notes_bp.route("/eliminar-nota/<int:id>", methods=["POST"])
def delete_note(id):
    note = Note.query.get_or_404(id)
    db.session.delete(note)
    db.session.commit()
    return redirect(url_for("notes.home"))
