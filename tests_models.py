import unittest

from app import create_app
from models import db, Note

class NoteTests(unittest.TestCase):
    # Pruebas unitarias para el modelo Note

    def setUp(self):
        # Configura la app y la DB antes de cada prueba
        self.app = create_app("config.TestConfig")
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()


    def test_create_note(self):
        # Prueba la creación de una nota
        with self.app.app_context():
            note_db = Note(title="Título", content="Contenido")
            db.session.add(note_db)
            db.session.commit()

            note = Note.query.first()
            self.assertEqual(note.title, "Título")
            self.assertEqual(note.content, "Contenido")


    def test_update_note(self):
        with self.app.app_context():
            # Crear nota
            note_db = Note(title="Original", content="Contenido original")
            db.session.add(note_db)
            db.session.commit()

            # Actualizar la nota
            note_db.title = "Actualizado"
            note_db.content = "Contenido actualizado"
            db.session.commit()

            # Consultar de nuevo desde la DB usando filter_by
            updated_note = Note.query.filter_by(id=note_db.id).first()
            self.assertEqual(updated_note.title, "Actualizado")
            self.assertEqual(updated_note.content, "Contenido actualizado")


    def test_delete_note(self):
        with self.app.app_context():
            # Crear nota
            note_db = Note(title="Título", content="Contenido")
            db.session.add(note_db)
            db.session.commit()

            # Eliminar nota
            db.session.delete(note_db)
            db.session.commit()

            # Consultar de nuevo desde la DB
            deleted_note = Note.query.filter_by(id=note_db.id).first()
            self.assertIsNone(deleted_note)

