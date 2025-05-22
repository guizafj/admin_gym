"""
formularios.py

Define los formularios utilizados en la aplicación Flask para la gestión de clientes.
Utiliza Flask-WTF y WTForms para la validación y manejo de formularios web.

Autor: Francisco Diaz Guiza
Fecha: 2025-05-17

Convenciones:
- Se sigue la guía de estilo PEP 8.
- Se documentan clases y campos.
"""

from flask_wtf import FlaskForm
from wtforms.fields.numeric import IntegerField
from wtforms.fields.simple import StringField, SubmitField, HiddenField
from wtforms.validators import DataRequired

class FormAgregar(FlaskForm):
    """
    Formulario para agregar o editar un cliente.

    Campos:
        id (HiddenField): Campo oculto para el identificador del cliente.
        nombre (StringField): Campo para el nombre del cliente (obligatorio).
        apellido (StringField): Campo para el apellido del cliente (obligatorio).
        membresia (IntegerField): Campo para el número de membresía (obligatorio).
        guardar (SubmitField): Botón para enviar el formulario.
    """
    id = HiddenField('id')
    nombre = StringField('Nombre', validators=[DataRequired()])
    apellido = StringField('Apellido', validators=[DataRequired()])
    membresia = IntegerField('Membresia', validators=[DataRequired()])
    guardar = SubmitField('Guardar')
