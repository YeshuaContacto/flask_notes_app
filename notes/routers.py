from flask import redirect, request, render_template, url_for, Blueprint, flash, session
from models import Note, db

# Crear blueprint para las rutas de notas
notes_bp = Blueprint("notes", __name__)

# ----------------------------
# Ruta: Home / Listado de notas
# ----------------------------
@notes_bp.route("/")
def home():
    # Verificar si el usuario está logueado
    if "user" not in session:
        flash("Para poder ver las notas debes iniciar sesión", "error")
        return redirect(url_for("auth.login"))

    # Obtener página actual desde query params
    page = request.args.get("page", 1, type=int)
    per_page = 9  # Notas por página

    # Consultar notas y paginarlas
    pagination = Note.query.order_by(Note.id.desc()).paginate(page=page, per_page=per_page)
    notes = pagination.items  # Notas de la página actual

    return render_template("home.html", notes=notes, pagination=pagination)

# ----------------------------
# Ruta: Crear nota
# ----------------------------
@notes_bp.route("/crear-nota", methods=["GET", "POST"])
def create_note():
    if request.method == "POST":
        # Obtener datos del formulario
        title = request.form.get("title", "")
        content = request.form.get("content", "")

        # Validaciones
        if not len(title.strip()) > 2:
            flash("El título es muy corto, minimo 2 caracteres", "error")
            return render_template("note_form.html")
        
        if len(title.strip()) > 30:
            flash("El título es muy largo, máximo 30 caracteres", "error")
            return render_template("note_form.html")

        if not len(content.strip()) > 3:
            flash("El contenido es muy corto, minimo 3 caracteres", "error")
            return render_template("note_form.html")

        # Crear y guardar nota en la DB
        note_db = Note(title=title, content=content)
        db.session.add(note_db)
        db.session.commit()
        flash("Nota creada", "success")
        return redirect(url_for("notes.home"))

    # GET: Mostrar formulario vacío
    return render_template("note_form.html")

# ----------------------------
# Ruta: Editar nota
# ----------------------------
@notes_bp.route("/editar-nota/<int:id>", methods=["GET", "POST"])
def edit_note(id):
    # Obtener nota o devolver 404 si no existe
    note = Note.query.get_or_404(id)

    if request.method == "POST":
        # Obtener datos del formulario
        title = request.form.get("title", "")
        content = request.form.get("content", "")

        # Validaciones
        if not len(title.strip()) > 2:
            flash("El título es muy corto, minimo 2 caracteres", "error")
            return render_template("edit_note.html", note=note)
        
        if len(title.strip()) > 30:
            flash("El título es muy largo, máximo 30 caracteres", "error")
            return render_template("edit_note.html", note=note)

        if not len(content.strip()) > 3:
            flash("El contenido es muy corto, minimo 3 caracteres", "error")
            return render_template("edit_note.html", note=note)

        # Actualizar y guardar cambios
        note.title = title
        note.content = content
        db.session.commit()
        return redirect(url_for("notes.home"))

    # GET: Mostrar formulario con datos de la nota
    return render_template("edit_note.html", note=note)

# ----------------------------
# Ruta: Eliminar nota
# ----------------------------
@notes_bp.route("/eliminar-nota/<int:id>", methods=["POST"])
def delete_note(id):
    # Obtener nota o devolver 404 si no existe
    note = Note.query.get_or_404(id)

    # Eliminar de la DB
    db.session.delete(note)
    db.session.commit()
    return redirect(url_for("notes.home"))
