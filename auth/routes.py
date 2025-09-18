from flask import Blueprint, request, render_template, redirect, url_for, flash, session

# Crear blueprint para autenticación
auth_bp = Blueprint("auth", __name__)

# ----------------------------
# Ruta: Login
# ----------------------------
@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    """
    Gestiona el inicio de sesión del usuario.
    
    GET: Muestra el formulario de login.
    POST: Valida el usuario y establece la sesión.
    """
    if request.method == "POST":
        # Obtener usuario desde el formulario
        username = request.form["username"]

        # Validación simple (ejemplo)
        if username == "admin":
            # Guardar usuario en sesión
            session["user"] = username
            return redirect(url_for("notes.home"))
        else:
            # Usuario no permitido
            flash("Usuario no permitido", "error")

    # Mostrar formulario de login
    return render_template("login.html")

# ----------------------------
# Ruta: Logout
# ----------------------------
@auth_bp.route("/logout")
def logout():
    """
    Cierra la sesión del usuario.
    - Elimina la información de usuario de la sesión.
    - Muestra un mensaje flash de éxito.
    - Redirige al login.
    """
    session.pop("user", None)  # Eliminar clave 'user' de la sesión
    flash("Te has deslogueado correctamente", "success")
    return redirect(url_for("auth.login"))
