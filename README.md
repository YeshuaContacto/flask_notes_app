# 📝 Flask Notes App  

Aplicación web sencilla desarrollada con **Flask** para crear y gestionar notas.  
Este proyecto es ideal como base para practicar el desarrollo con Python y Flask.  

---

## 🚀 Características  
- Creación y gestión de notas.  
- Estructura simple y fácil de escalar.  
- Entorno virtual para aislar dependencias.  

---

## ⚙️ Instalación  

1. Clonar este repositorio:  
   ```bash
   git clone https://github.com/tu_usuario/flask_notes_app.git
   cd flask_notes_app

2. Crear y activar un entorno virtual:
   ```bash
    python -m venv env
    source env/bin/activate    # Linux/Mac
    env\Scripts\activate       # Windows

3. Instalar dependencias:
   ```bash
    pip install -r requirements.txt

## ▶️ Ejecución

1. Ejecutar la aplicación:
   ```bash
   python app.py

3. Abrir en el navegador:
   ```bash
   http://127.0.0.1:5000

## 📂 Estructura del Proyecto
   ```bash
   flask_notes_app/
   ├── auth/
   │   └── routers.py       # Rutas de autenticación (login, logout)
   ├── instance/
   │   └── test_notes.db    # Base de datos de pruebas
   ├── notes/
   │   └── routers.py       # Rutas para notas
   ├── templates/           # Carpeta con los templates HTML
   │   ├── base.html        # Template base que heredan otros templates
   │   ├── edit_note.html   # Template para editar notas
   │   ├── home.html        # Template principal con listado de notas
   │   ├── login.html       # Template de login
   │   └── note_form.html   # Template para crear nuevas notas (sin espacios)
   ├── env/                 # Entorno virtual (ignorado en Git)
   ├── .gitignore           # Archivos/carpetas ignoradas por Git
   ├── app.py               # Punto de entrada de la aplicación
   ├── config.py            # Configuraciones de Flask
   ├── models.py            # Modelos de la base de datos
   ├── notes.sqlite         # Base de datos principal
   ├── README.md            # Documentación del proyecto
   ├── requirements.txt     # Dependencias del proyecto
   │── test_notes.db        # Base de datos de pruebas
   └── test_models.py       # Pruebas unitarias
   ```

## 🛠️ Tecnologías

- Python  
- Flask  

## 🤝 Contribución
¡Las contribuciones son bienvenidas!

1. Haz un fork del repositorio

2. Crea una rama:
   ```bash
   git checkout -b feature/nueva-funcionalidad

3. Haz un commit:
   ```bash
   git commit -m 'Agrego nueva funcionalidad'

4. Haz un push:
   ```bash
   git push origin feature/nueva-funcionalidad

5. Abre un Pull Request 🚀

## 📄 Licencia
Este proyecto se distribuye bajo la licencia MIT.





